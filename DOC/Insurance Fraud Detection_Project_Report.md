# Insurance Fraud Detection using Machine Learning - Project Report

## Executive Summary

This project implements an end-to-end machine learning pipeline to detect fraudulent automobile insurance claims. Using historical claim data and multiple machine learning algorithms, the system learns patterns associated with fraud and predicts whether a new claim is **Fraudulent or Genuine**.

The final model is integrated into a simple web interface that allows users to input claim information and receive instant predictions. The system helps insurance companies reduce financial losses, improve investigation efficiency, and automate fraud detection.

---

# Project Overview

**Project Title:** Insurance Fraud Detection using Machine Learning  
**Domain:** Machine Learning / Financial Fraud Detection  
**Platform:** GitHub Academic Project  

### Project Metrics

- **Complexity:** Medium–High
- **Dataset Size:** ~15,000 insurance claim records
- **Features Used:** 18
- **Overall Progress:** 90%
- **Algorithms Tested:** 6 Machine Learning Models

---

# Problem Statement

Insurance fraud is a major issue in the insurance industry, causing billions of dollars in losses every year. Fraudulent claims increase operational costs and make insurance more expensive for honest customers.

Traditionally, insurance claims are verified manually by investigators. However, manual investigation is time-consuming, costly, and inefficient when dealing with thousands of claims.

Detecting fraudulent claims among legitimate ones is challenging because fraud patterns are often complex and hidden in large datasets.

Therefore, there is a need for an **automated fraud detection system** that can analyze historical claim data and quickly predict whether a claim is **fraudulent or genuine**.

---

# Solution Overview

This project develops a **Machine Learning-based Insurance Fraud Detection System** that:

- Analyzes historical claim data
- Detects patterns associated with fraud
- Predicts whether a claim is **Fraudulent or Genuine**
- Assists investigators in identifying high-risk claims

The solution includes:

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering and encoding
- Handling class imbalance using **SMOTE**
- Training and evaluating multiple ML models
- Selecting the best performing model
- Deploying the model through a simple **HTML & CSS interface**

---

# Project Results

### Model Performance (Example Results)

| Model | Accuracy | Precision | Recall | F1 Score |
|------|----------|----------|-------|---------|
| Decision Tree | 88% | 84% | 86% | 85% |
| Random Forest | 91% | 89% | 90% | 89% |
| KNN | 87% | 83% | 84% | 83% |
| Logistic Regression | 89% | 86% | 88% | 87% |
| SVM | 90% | 88% | 89% | 88% |
| **Naive Bayes** | **92%** | **90%** | **91%** | **90%** |

### Technical Achievements

✅ Cleaned and processed a large insurance dataset  
✅ Performed detailed Exploratory Data Analysis (EDA)  
✅ Implemented multiple machine learning algorithms  
✅ Solved class imbalance using **SMOTE**  
✅ Performed hyperparameter tuning using **GridSearchCV**  
✅ Built a simple web interface for fraud prediction  
✅ Saved trained model using **Pickle** for deployment  

---

# Technology Stack

### Programming & Data Processing
- Python
- Pandas
- NumPy

### Machine Learning
- Scikit-learn
- SMOTE (Imbalanced-learn)

### Data Visualization
- Matplotlib
- Seaborn

### Model Deployment
- Pickle (.pkl)

### Frontend
- HTML
- CSS

### Version Control
- Git
- GitHub

---

# Machine Learning Pipeline

# Machine Learning Pipeline

1. **Dataset Collection**
2. **Data Cleaning**
3. **Exploratory Data Analysis (EDA)**
4. **Feature Engineering**
5. **Categorical Feature Encoding**
6. **Train-Test Split**
7. **SMOTE (Class Imbalance Handling)**
8. **Feature Scaling**
9. **Train Multiple ML Models**
10. **Model Evaluation**
11. **Hyperparameter Tuning**
12. **Best Model Selection**
13. **Model Saving (.pkl)**
14. **Web Interface for Fraud Prediction**

# Key Features

### Automated Fraud Detection

- Predicts fraud automatically using machine learning
- Reduces dependency on manual claim investigation
- Provides fast and accurate predictions

### Pattern Recognition

- Detects hidden patterns in insurance claim data
- Identifies suspicious claim behavior

### Efficient Claim Processing

- Filters high-risk claims automatically
- Investigators focus only on suspicious cases

### User Interface

- Simple interface built with **HTML and CSS**
- Allows users to input claim details
- Displays prediction as **Fraud or Genuine**

---

# Project Milestones

### Milestone 1: Dataset Collection

- Collected automobile insurance fraud dataset
- Verified data quality and structure
- Identified 33 initial features

---

### Milestone 2: Data Cleaning & Preprocessing

- Removed unnecessary columns
- Handled missing values
- Removed duplicate records
- Performed outlier detection using **IQR**

---

### Milestone 3: Exploratory Data Analysis (EDA)

- Analyzed fraud vs non-fraud distribution
- Generated visualizations:
  - Pie charts
  - Bar plots
  - Boxplots
  - Heatmaps
- Identified relationships between features and fraud

---

### Milestone 4: Model Development

- Encoded categorical variables
- Applied **SMOTE** to balance dataset
- Trained multiple machine learning models:
  - Decision Tree
  - Random Forest
  - KNN
  - Logistic Regression
  - Naive Bayes
  - SVM

---

### Milestone 5: Model Deployment

- Selected best performing model
- Saved model using **Pickle**
- Built HTML interface for prediction
- Tested end-to-end workflow

---

# Expected Impact

### Operational Benefits

- Faster fraud detection
- Reduced manual investigation workload
- Improved claim processing efficiency

### Financial Benefits

- Prevents fraudulent payouts
- Reduces financial losses
- Improves profitability for insurance companies

### Industry Benefits

- Protects honest policyholders
- Strengthens fraud prevention systems
- Encourages data-driven decision making

---

# Future Enhancements

1. Integration with real-time insurance claim systems
2. Deep learning models for advanced fraud detection
3. API-based prediction service
4. Cloud deployment (AWS / GCP / Azure)
5. Dashboard for fraud analytics and monitoring

---

# Conclusion

This project demonstrates how machine learning can be applied to detect fraudulent insurance claims effectively. By analyzing historical claim data and training predictive models, the system can identify suspicious claims quickly and accurately.

The solution helps insurance companies reduce fraud-related losses, improve operational efficiency, and automate claim verification processes.

---

# Author

Project developed as part of an academic project titled:

**Insurance Fraud Detection Using Machine Learning**
