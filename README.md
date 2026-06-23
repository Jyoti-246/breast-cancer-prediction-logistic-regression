# Breast Cancer Prediction using Logistic Regression

## Overview

This project uses Machine Learning to predict whether a breast tumor is benign or malignant using Logistic Regression. The model is trained on the Breast Cancer Wisconsin dataset and evaluated using accuracy metrics, confusion matrix, and k-fold cross-validation.

## Features

- Data preprocessing and cleaning
- Logistic Regression classification
- Model evaluation using confusion matrix
- Accuracy score calculation
- 10-Fold Cross Validation
- Model deployment using Streamlit

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Matplotlib
- Seaborn

## Dataset

The project uses the Breast Cancer Wisconsin Dataset containing various tumor characteristics used to classify tumors as benign or malignant.

## Model Performance

- Logistic Regression Classifier
- Cross Validation Mean Accuracy: 96.70%
- Standard Deviation: 1.97%

## Project Structure

```
Breast-Cancer-Prediction/
│
├── app.py
├── breast_cancer_model.pkl
├── breast_cancer.csv
├── Cancer_prediction_Logistic.ipynb
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone <repository-url>
cd Breast-Cancer-Prediction
pip install -r requirements.txt
```

## Run Locally

```bash
streamlit run app.py
```

## Future Improvements

- Feature Scaling
- Hyperparameter Tuning
- ROC-AUC Analysis
- Model Comparison with Random Forest and KNN
- Cloud Deployment

## Author

Jyoti Kedia
BCA Student | Machine Learning Enthusiast
