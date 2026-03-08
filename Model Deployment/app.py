# ── Import the libraries ──────────────────────────────────────────
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

# ── Load the saved model ──────────────────────────────────────────
model        = pickle.load(open('deployment/fraud_model.pkl',  'rb'))
scaler       = pickle.load(open('deployment/scaler.pkl',       'rb'))
feature_cols = pickle.load(open('deployment/feature_cols.pkl', 'rb'))

# ── An object of Flask class is our WSGI application ─────────────
# Flask constructor takes the name of current module (__name__)
app = Flask(__name__)

# ── Ordinal encoding maps (same order as notebook) ────────────────
ORD_MAPS = {
    'Days:Policy-Accident': ['none','1 to 7','8 to 15','15 to 30','more than 30'],
    'Days:Policy-Claim':    ['none','1 to 7','8 to 15','15 to 30','more than 30'],
    'PastNumberOfClaims':   ['none','1','2 to 4','more than 4'],
    'NumberOfSuppliments':  ['none','1 to 2','3 to 5','more than 5'],
    'AgeOfVehicle':         ['new','2 years','3 years','4 years',
                             '5 years','6 years','7 years','more than 7'],
    'VehiclePrice':         ['less than 20,000','20,000 to 29,000','30,000 to 39,000',
                             '40,000 to 59,000','60,000 to 69,000','more than 69,000'],
    'AddressChange-Claim':  ['no change','under 6 months','1 year',
                             '2 to 3 years','4 to 8 years'],
}


def preprocess(form):
    """
    Encode form values using the EXACT same pandas pipeline as the notebook.

    Notebook pipeline:
      1. Binary map  → PoliceReportFiled, Fault
      2. Ordinal     → pd.Categorical(...).codes
      3. One-hot     → pd.get_dummies(drop_first=True)
      4. Align cols  → reindex to feature_cols, fill missing with 0
    """

    # ── Build raw single-row DataFrame (same column names as CSV) ─
    df = pd.DataFrame([{
        'AccidentArea':         form.get('AccidentArea',        'Urban'),
        'Sex':                  form.get('Sex',                 'Male'),
        'MaritalStatus':        form.get('MaritalStatus',       'Single'),
        'Age':                  int(form.get('Age', 30)),
        'Fault':                form.get('Fault',               'Policy Holder'),
        'PolicyType':           form.get('PolicyType',          'Sport - Liability'),
        'VehiclePrice':         form.get('VehiclePrice',        'less than 20,000'),
        'Deductible':           int(form.get('Deductible',      400)),
        'DriverRating':         int(form.get('DriverRating',    1)),
        'Days:Policy-Accident': form.get('Days:Policy-Accident','none'),
        'Days:Policy-Claim':    form.get('Days:Policy-Claim',   'none'),
        'PastNumberOfClaims':   form.get('PastNumberOfClaims',  'none'),
        'AgeOfVehicle':         form.get('AgeOfVehicle',        'new'),
        'PoliceReportFiled':    form.get('PoliceReportFiled',   'No'),
        'AgentType':            form.get('AgentType',           'External'),
        'NumberOfSuppliments':  form.get('NumberOfSuppliments', 'none'),
        'AddressChange-Claim':  form.get('AddressChange-Claim', 'no change'),
    }])

    # ── Step 1: Binary encoding (same as notebook) ────────────────
    df['PoliceReportFiled'] = df['PoliceReportFiled'].map({'No': 0, 'Yes': 1})
    df['Fault']             = df['Fault'].map({'Policy Holder': 0, 'Third Party': 1})

    # ── Step 2: Ordinal encoding (pd.Categorical → codes) ─────────
    for col, cats in ORD_MAPS.items():
        df[col] = pd.Categorical(df[col], categories=cats, ordered=True).codes

    # ── Step 3: One-hot encoding — drop_first=True (same as notebook)
    nominal_cols = ['AccidentArea', 'Sex', 'MaritalStatus', 'PolicyType', 'AgentType']
    df = pd.get_dummies(df, columns=nominal_cols, drop_first=True)

    # ── Step 4: Convert bool columns to int ───────────────────────
    for col in df.select_dtypes(include=['bool']).columns:
        df[col] = df[col].astype(int)

    # ── Step 5: Align to training feature_cols exactly ────────────
    # This is the KEY fix — adds missing dummy cols as 0,
    # removes any extra cols, and reorders to match training exactly
    df = df.reindex(columns=feature_cols, fill_value=0)

    return df


# ── Render HTML page ──────────────────────────────────────────────
# '/' URL is bound to index() — when home page opens, index.html renders
@app.route('/')
def index():
    return render_template('index.html')


# ── Retrieve values from UI and predict ───────────────────────────
# Routing app to predict() — retrieves all values from HTML via POST
# Values stored in array → passed to model.predict() → result rendered
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the values from the HTML page using POST request
    form_data = request.form.to_dict()

    # Preprocess and build feature array (same pipeline as notebook)
    X = preprocess(form_data)

    # Scale the array (same scaler used during training)
    X_scaled = scaler.transform(X)

    # Pass array to model.predict() — returns the prediction
    prediction_raw = model.predict(X_scaled)[0]
    proba          = model.predict_proba(X_scaled)[0]

    # Map prediction to readable label
    prediction = 'Fraud' if int(prediction_raw) == 1 else 'Genuine'
    confidence = round(float(max(proba)) * 100, 1)
    fraud_prob = round(float(proba[1]) * 100, 1) if len(proba) > 1 else 0.0

    if fraud_prob >= 70:   risk = 'High'
    elif fraud_prob >= 40: risk = 'Medium'
    else:                  risk = 'Low'

    # Render prediction value to result.html
    return render_template('result.html',
        prediction = prediction,
        confidence = confidence,
        fraud_prob = fraud_prob,
        risk       = risk,
        inputs     = form_data,
    )


# ── Main Function ─────────────────────────────────────────────────
# Steps to run:
# 1. Open Anaconda Prompt
# 2. Navigate to your project folder:  cd path/to/your_project
# 3. Run:                               python app.py
# 4. Open browser:                      http://127.0.0.1:5000
if __name__ == '__main__':
    app.run(debug=True)
