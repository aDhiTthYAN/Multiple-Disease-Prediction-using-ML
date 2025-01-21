# Disease Prediction System using Machine Learning

This repository contains a machine learning-based application that predicts the likelihood of **Diabetes** and **Heart Disease** using user-provided inputs. The project uses various machine learning models, including Random Forest, SVM, Logistic Regression, and Gradient Boosting, to classify data and provide accurate predictions.

## Project Overview

The project is designed to help in predicting **Diabetes** and **Heart Disease** based on a set of input features. The data is preprocessed and standardized using techniques like SMOTE for handling class imbalance. Models are trained and hyperparameter-tuned to achieve high accuracy and provide reliable results.

The final models are saved and deployed using **Streamlit** for easy user interaction. The user can input values via a web interface, and the model will output the prediction for diabetes or heart disease.

## Dataset Information

1. **Diabetes Dataset**: The dataset used for predicting diabetes contains multiple features such as glucose levels, BMI, insulin, and other health-related attributes to determine if an individual is diabetic.
    
    - **Outcome** column:
        - 0 → Non-Diabetic
        - 1 → Diabetic

2. **Heart Disease Dataset**: The dataset used for predicting heart disease contains various features such as age, sex, chest pain type, blood pressure, cholesterol levels, and other relevant factors to predict heart disease.
    
    - **Prediction Output**:
        - 0 → No Heart Disease
        - 1 → Heart Disease Present

## Libraries Used

- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Scikit-learn**: For machine learning models, preprocessing, and evaluation.
- **Imbalanced-learn**: For handling class imbalance using SMOTE.
- **Streamlit**: For the web-based user interface.
- **Seaborn/Matplotlib**: For data visualization.

## Installation

### Requirements

To run the application locally, you must have Python 3.7+ installed along with the following packages:

- pandas
- numpy
- scikit-learn
- imbalanced-learn
- streamlit
- matplotlib
- seaborn

You can install the necessary packages using `pip`:

```bash
pip install pandas numpy scikit-learn imbalanced-learn streamlit matplotlib seaborn

