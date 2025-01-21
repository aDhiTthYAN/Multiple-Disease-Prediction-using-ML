# Disease Prediction System using Machine Learning

This repository contains a machine learning-based application that predicts the likelihood of **Diabetes** and **Heart Disease** using user-provided inputs. The project uses various machine learning models, including Random Forest, SVM, Logistic Regression, and Gradient Boosting, to classify data and provide accurate predictions.

## Project Overview

The project is designed to help in predicting **Diabetes** and **Heart Disease** based on a set of input features. The data is preprocessed and standardized using techniques like SMOTE for handling class imbalance. Models are trained and hyperparameter-tuned to achieve high accuracy and provide reliable results. The final models are saved and deployed using **Streamlit** for easy user interaction. The user can input values via a web interface, and the model will output the prediction for diabetes or heart disease.

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

## Model Training

The models are trained using the following steps:

1. **Data Preprocessing**:
    - Data is cleaned by checking for missing values and handling them.
    - Features are scaled using **StandardScaler**.
    - **SMOTE** is applied to handle class imbalance in the training dataset.

2. **Model Training**:
    - Various models are used: Random Forest, Support Vector Machine (SVM), Logistic Regression, Gradient Boosting.
    - Hyperparameters for each model are tuned using **RandomizedSearchCV**.
    - Cross-validation is performed to ensure the models' performance is consistent.

3. **Model Evaluation**:
    - The models are evaluated using accuracy, classification report, and confusion matrix.
    - The best-performing model is selected for final prediction.

4. **Model Deployment**:
    - The best model for each disease prediction (Diabetes and Heart Disease) is serialized using **Pickle**.
    - A **Streamlit** app is created where users can input their details and get the prediction result.

## Usage

### Running the Streamlit App

1. After cloning this repository, open a terminal or command prompt.
2. Navigate to the directory where the `app.py` is located.
3. Run the following command:

    ```bash
    streamlit run app.py
    ```

4. A new tab will open in your browser, allowing you to enter the necessary details and get predictions for **Diabetes** and **Heart Disease**.

### Diabetes Prediction

For the **Diabetes Prediction**, the following features are required:

- Number of Pregnancies
- Glucose Level
- Blood Pressure value
- Skin Thickness value
- Insulin Level
- BMI value
- Diabetes Pedigree Function value
- Age

### Heart Disease Prediction

For the **Heart Disease Prediction**, the following features are required:

- Age
- Sex (0: Female, 1: Male)
- Chest Pain types
- Resting Blood Pressure
- Serum Cholestoral in mg/dl
- Fasting Blood Sugar > 120 mg/dl
- Resting Electrocardiographic results
- Maximum Heart Rate achieved
- Exercise Induced Angina
- ST depression induced by exercise
- Slope of the peak exercise ST segment
- Major vessels colored by fluoroscopy
- thal (0: normal, 1: fixed defect, 2: reversible defect)

### Example

#### Diabetes Prediction:

```python
input_data = (4, 110, 92, 0, 0, 37.6, 8.191, 30)  # Input sample data
prediction = diabetes_model.predict(input_data)



