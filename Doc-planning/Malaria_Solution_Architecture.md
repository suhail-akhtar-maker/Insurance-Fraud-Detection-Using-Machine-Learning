# Insurance Fraud Detection using Machine Learning - Solution Architecture

## Architecture Overview

The system follows a layered architecture that connects the business problem of detecting fraudulent insurance claims with a machine learning–based technology solution.

The architecture describes the end-to-end process from a user entering insurance claim details to the system delivering a prediction indicating whether the claim is **Fraudulent or Genuine**.

The system integrates a machine learning model with a simple web interface to provide real-time fraud detection.

---

# Architectural Layers

## Layer 1: User Interface Layer

### Components
- Insurance Investigator / User
- Web Interface (HTML & CSS)

### Responsibility

- Allows users to input insurance claim details
- Accessible through a simple web interface
- Displays prediction results to the user
- Requires minimal technical knowledge to operate

The interface serves as the entry point where claim information is submitted for fraud analysis.

---

## Layer 2: Application Processing Layer

### Components
- Input Validation Module
- Data Preprocessing Module
- Feature Processing Module

### Responsibility

- Receives claim information from the user interface
- Validates input values to ensure correct format
- Converts input data into a structured format for model prediction
- Applies preprocessing steps similar to training pipeline:
  - Encoding categorical variables
  - Feature scaling
  - Feature alignment with trained model

This layer prepares the input data before passing it to the machine learning model.

---

## Layer 3: Machine Learning Model Layer

### Components
- Trained Machine Learning Model
- Prediction Engine
- Scaler and Feature Encoder

### Responsibility

- Loads the trained model file (`fraud_model.pkl`)
- Applies the same preprocessing used during training
- Performs prediction using machine learning algorithms

Models used in development include:

- Decision Tree
- Random Forest
- K-Nearest Neighbors
- Logistic Regression
- Naive Bayes
- Support Vector Machine

The final selected model generates a prediction indicating whether a claim is **Fraudulent or Genuine**.

---

## Layer 4: Data Storage Layer

### Components
- Insurance Claims Dataset
- Trained Model File
- Feature Columns File
- Scaler Object

### Responsibility

- Stores historical insurance claim data used for model training
- Stores trained machine learning model in `.pkl` format
- Stores preprocessing objects such as:
  - Feature columns
  - Scaler
  - Encoders

These files ensure that predictions follow the same pipeline used during training.

---

## Layer 5: Output Delivery Layer

### Components
- Prediction Result Page
- Fraud / Genuine Label Display

### Responsibility

- Displays prediction result to the user
- Shows whether the claim is:

  **Fraudulent**  
  **or**  
  **Genuine**

- Provides quick decision support for investigators

This layer communicates the final prediction back to the user interface.

---

# Data Flow

1. **User Input**  
   User enters insurance claim information in the web interface.

2. **Input Validation**  
   The application validates the entered data for correctness.

3. **Data Preprocessing**  
   Input data is processed using:
   - Encoding of categorical variables
   - Feature scaling
   - Feature alignment with training dataset

4. **Model Prediction**  
   The trained machine learning model performs prediction.

5. **Fraud Classification**  
   The system determines whether the claim is **Fraudulent or Genuine**.

6. **Result Display**  
   The prediction result is displayed to the user.

---

# Technology Stack

## Frontend Layer
- HTML
- CSS

## Backend & Processing
- Python
- Pandas
- NumPy

## Machine Learning
- Scikit-learn
- SMOTE (Imbalanced-learn)

## Data Visualization
- Matplotlib
- Seaborn

## Model Persistence
- Pickle (.pkl)

## Version Control
- Git
- GitHub

---

# Performance Metrics

The machine learning models were evaluated using multiple metrics:

| Metric | Description |
|------|-------------|
| Accuracy | Overall correctness of predictions |
| Precision | Correct fraud predictions among predicted fraud cases |
| Recall | Ability to correctly detect fraudulent claims |
| F1 Score | Balance between precision and recall |
| ROC-AUC | Model ability to distinguish fraud vs genuine claims |

These metrics ensure reliable and effective fraud detection.

---

# Deployment Environment

## Local Deployment
- Python environment
- Model prediction via local interface
- Suitable for testing and demonstrations

## Web Deployment (Future Scope)
- Integration with insurance claim management systems
- Cloud deployment on AWS / GCP / Azure
- Real-time fraud detection services

---

# Key Design Decisions

### Multiple Model Comparison
Several machine learning models were tested to identify the best performing algorithm for fraud detection.

### Handling Imbalanced Data
SMOTE was used to address the imbalance between fraudulent and genuine claims.

### Feature Engineering
Categorical features were encoded using appropriate encoding techniques to improve model performance.

### Lightweight Deployment
The system uses a simple HTML and CSS interface to ensure ease of use and quick deployment.

### Automated Fraud Detection
The solution enables fast and reliable fraud detection without requiring extensive manual investigation.
