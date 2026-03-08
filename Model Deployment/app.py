# Import the libraries 
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('deployment/fraud_model.pkl',  'rb'))
scaler = pickle.load(open('deployment/scaler.pkl',       'rb'))
feature_cols = pickle.load(open('deployment/feature_cols.pkl', 'rb'))


app = Flask(__name__)


ORD_MAPS = {'Days:Policy-Accident': ['none','1 to 7','8 to 15','15 to 30','more than 30'],'Days:Policy-Claim': ['none','1 to 7','8 to 15','15 to 30','more than 30'],'PastNumberOfClaims': ['none','1','2 to 4','more than 4'],'NumberOfSuppliments':  ['none','1 to 2','3 to 5','more than 5'],'AgeOfVehicle': ['new','2 years','3 years','4 years','5 years','6 years','7 years','more than 7'],'VehiclePrice': ['less than 20,000','20,000 to 29,000','30,000 to 39,000','40,000 to 59,000','60,000 to 69,000','more than 69,000'],'AddressChange-Claim':  ['no change','under 6 months','1 year','2 to 3 years','4 to 8 years'],}

def preprocess(form):
   
    df = pd.DataFrame([{'AccidentArea':form.get('AccidentArea','Urban'),'Sex':form.get('Sex','Male'),'MaritalStatus':form.get('MaritalStatus','Single'),'Age':int(form.get('Age', 30)),'Fault':form.get('Fault','Policy Holder'),'PolicyType':form.get('PolicyType','Sport - Liability'),'VehiclePrice':form.get('VehiclePrice','less than 20,000'),'Deductible':int(form.get('Deductible',400)),'DriverRating':  int(form.get('DriverRating',    1)),'Days:Policy-Accident': form.get('Days:Policy-Accident','none'),'Days:Policy-Claim':    form.get('Days:Policy-Claim',   'none'),'PastNumberOfClaims':   form.get('PastNumberOfClaims',  'none'),'AgeOfVehicle':form.get('AgeOfVehicle','new'),'PoliceReportFiled':form.get('PoliceReportFiled','No'),'AgentType':form.get('AgentType','External'),'NumberOfSuppliments':form.get('NumberOfSuppliments', 'none'),'AddressChange-Claim':  form.get('AddressChange-Claim', 'no change'),}])

    df['PoliceReportFiled'] = df['PoliceReportFiled'].map({'No': 0, 'Yes': 1})
    df['Fault'] = df['Fault'].map({'Policy Holder': 0, 'Third Party': 1})
   
    for col, cats in ORD_MAPS.items():
        df[col] = pd.Categorical(df[col], categories=cats, ordered=True).codes

    nominal_cols = ['AccidentArea', 'Sex', 'MaritalStatus', 'PolicyType', 'AgentType']
    df = pd.get_dummies(df, columns=nominal_cols, drop_first=True)
    
    for col in df.select_dtypes(include=['bool']).columns:
        df[col] = df[col].astype(int)
    df = df.reindex(columns=feature_cols, fill_value=0)
    return df
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    form_data = request.form.to_dict()
        X = preprocess(form_data)
    X_scaled = scaler.transform(X)

    prediction_raw = model.predict(X_scaled)[0]
    proba = model.predict_proba(X_scaled)[0]

    prediction = 'Fraud' if int(prediction_raw) == 1 else 'Genuine'
    confidence = round(float(max(proba)) * 100, 1)
    fraud_prob = round(float(proba[1]) * 100, 1) if len(proba) > 1 else 0.0

    if fraud_prob >= 70:   risk = 'High'
    elif fraud_prob >= 40: risk = 'Medium'
    else:                  risk = 'Low'

    return render_template('result.html',prediction = prediction,confidence = confidence,fraud_prob = fraud_prob,risk = risk,inputs = form_data,)

if __name__ == '__main__':
    app.run(debug=True)
