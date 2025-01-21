

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/DELL/OneDrive/Documents/Multiple disease prediction/saved_models/diabetes_disease_model.sav','rb'))

heart_model = pickle.load(open('C:/Users/DELL/OneDrive/Documents/Multiple disease prediction/saved_models/heart_disease_model.sav','rb'))


with st.sidebar:
    selected = option_menu('Multiple disease prediction system',#side bar title
                           
                           ['Diabetes Prediction','Heart disease Prediction'],icons = ['activity','heart'],default_index=0)
    
#Diabetes Prediction Page

if (selected == "Diabetes Prediction"):
    #page title
    st.title("Diabetes prediction using Ml")
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')
 
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''
    if st.button("Diabetes Test Result"):
      try:
        # Convert inputs to float and make prediction
        dia_prediction = diabetes_model.predict([[float(Pregnancies), float(Glucose), float(BloodPressure),
                                                   float(SkinThickness), float(Insulin), float(BMI),
                                                   float(DiabetesPedigreeFunction), float(Age)]])
        if dia_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = "The person is not diabetic"
      except ValueError:
        diab_diagnosis = "Please enter valid numerical values for all fields."
    
    st.success(diab_diagnosis)
   
    
if (selected == "Heart disease Prediction"):
    #page title
    st.title("Heart disease Prediction using Ml")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.radio('Sex', ['0: Female', '1: Male'])

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
      try:
        # Convert user input to float
        user_input = [float(age), float(sex), float(cp), float(trestbps), float(chol), 
                      float(fbs), float(restecg), float(thalach), float(exang), 
                      float(oldpeak), float(slope), float(ca), float(thal)]
        
        # Make prediction
        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
      except ValueError:
        heart_diagnosis = "Please enter valid numerical values for all fields."
    
    # Display the result
    st.success(heart_diagnosis)
    

