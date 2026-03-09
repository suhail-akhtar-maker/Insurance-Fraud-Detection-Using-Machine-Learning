# Car Insurance Claims Fraud Detection - Project Planning

## Project Overview
Project Title: Car Insurance Claims Fraud Detection  
Project Complexity: Medium–High  
Project Duration: 24 Days  
Current Progress: 90%

This project develops a **Machine Learning system that detects fraudulent car insurance claims** using historical claim data.  
The system analyzes claim features such as policy type, accident area, driver rating, and past claims to predict whether a claim is **Fraudulent or Genuine**.

The final system includes:
- Data preprocessing and feature engineering
- Multiple machine learning models
- Hyperparameter tuning
- Model comparison and evaluation
- Deployment-ready trained model
- Web interface displaying **Fraud / Genuine prediction**

---

# Sprints

## Sprint 1: Data Collection & Preparation (Days 1–6)

Tasks completed:

- Load **Car Insurance Claims dataset** (`carclaims.csv`)
- Inspect dataset structure (33 columns, 15,420 records)
- Remove irrelevant columns such as:
  - PolicyNumber
  - RepNumber
  - Make
  - BasePolicy
  - VehicleCategory
  - Year
- Clean dataset by:
  - Removing invalid age values
  - Handling missing values using median and mode
- Detect and remove outliers using **IQR method**
- Reduce dataset noise and improve data quality

Result:
- Final cleaned dataset with **14,408 records and 18 columns**

**Story Points: 20**

---

## Sprint 2: Exploratory Data Analysis (EDA) (Days 7–12)

Tasks completed:

- Analyze fraud vs non-fraud distribution
- Visualize class imbalance (Fraud ≈ 5.7%)
- Perform **Chi-Square tests** for categorical variables
- Generate visualizations:
  - Pie charts for fraud distribution
  - Bar charts for claim counts
  - Boxplots and violin plots
  - KDE distribution plots
  - Pairplots for numeric relationships
  - Heatmaps for feature correlations
- Identify patterns between fraud cases and features such as:
  - Policy Type
  - Accident Area
  - Fault
  - Driver Rating

**Story Points: 20**

---

## Sprint 3: Feature Engineering & Model Development (Days 13–18)

Tasks completed:

### Feature Engineering

- Encode binary variables:
  - PoliceReportFiled
  - Fault

- Apply **Ordinal Encoding** for ordered features:
  - Days:Policy-Accident
  - Days:Policy-Claim
  - PastNumberOfClaims
  - NumberOfSuppliments
  - AgeOfVehicle
  - VehiclePrice
  - AddressChange-Claim

- Apply **One-Hot Encoding** for nominal features:
  - AccidentArea
  - Sex
  - MaritalStatus
  - PolicyType
  - AgentType

- Remove:
  - Duplicate records
  - Near-zero variance features
  - Highly correlated features

Final dataset:
- **18 selected features**

### Data Preparation

- Train/Test split (80% / 20%)
- Handle class imbalance using **SMOTE**
- Apply **StandardScaler** for feature scaling

### Machine Learning Models Trained

The following algorithms were trained and evaluated:

1. Decision Tree
2. Random Forest
3. K-Nearest Neighbors (KNN)
4. Logistic Regression
5. Naive Bayes
6. Support Vector Machine (SVM)

Evaluation metrics used:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

**Story Points: 20**

---

## Sprint 4: Model Evaluation, Tuning & Deployment (Days 19–24)

### Performance Testing

Models were compared using:

- Confusion matrices
- ROC curves
- Recall comparison
- F1 score comparison
- ROC-AUC scores

### Hyperparameter Tuning

GridSearchCV was applied for:

- Decision Tree
- Random Forest
- Logistic Regression

Best parameters were selected based on **Recall score**, which is important for fraud detection.

### Final Model Selection

Best performing model:

**Naive Bayes**

Performance highlights:

- High fraud detection recall
- Balanced model performance
- Fast prediction speed

### Model Deployment Preparation

Saved deployment files:
