
import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the trained model
filename = 'pages/lung_cancer_prediction_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

@st.cache_data
def predict_lung_cancer(features):
    return loaded_model.predict([features])

st.title("Lung Cancer Predictor 💊👩🏻‍⚕️")
st.subheader("Enter details to predict the likelihood of lung cancer:")

# Input fields for features
gender = st.selectbox("Gender:", ['Male', 'Female'])
age = st.number_input("Age:", min_value=0)
smoking = st.selectbox("Smoking:", ['No', 'Yes'])
yellow_fingers = st.selectbox("Yellow Fingers:", ['No', 'Yes'])
anxiety = st.selectbox("Anxiety:", ['No', 'Yes'])
peer_pressure = st.selectbox("Peer Pressure:", ['No', 'Yes'])
chronic_disease = st.selectbox("Chronic Disease:", ['No', 'Yes'])
fatigue = st.selectbox("Fatigue:", ['No', 'Yes'])
allergy = st.selectbox("Allergy:", ['No', 'Yes'])
wheezing = st.selectbox("Wheezing:", ['No', 'Yes'])
alcohol_consuming = st.selectbox("Alcohol Consuming:", ['No', 'Yes'])
coughing = st.selectbox("Coughing:", ['No', 'Yes'])
shortness_of_breath = st.selectbox("Shortness of Breath:", ['No', 'Yes'])
swallowing_difficulty = st.selectbox("Swallowing Difficulty:", ['No', 'Yes'])
chest_pain = st.selectbox("Chest Pain:", ['No', 'Yes'])

# Convert categorical features to numerical
gender_num = 1 if gender == 'Male' else 0
smoking_num = 1 if smoking == 'Yes' else 0
yellow_fingers_num = 1 if yellow_fingers == 'Yes' else 0
anxiety_num = 1 if anxiety == 'Yes' else 0
peer_pressure_num = 1 if peer_pressure == 'Yes' else 0
chronic_disease_num = 1 if chronic_disease == 'Yes' else 0
fatigue_num = 1 if fatigue == 'Yes' else 0
allergy_num = 1 if allergy == 'Yes' else 0
wheezing_num = 1 if wheezing == 'Yes' else 0
alcohol_consuming_num = 1 if alcohol_consuming == 'Yes' else 0
coughing_num = 1 if coughing == 'Yes' else 0
shortness_of_breath_num = 1 if shortness_of_breath == 'Yes' else 0
swallowing_difficulty_num = 1 if swallowing_difficulty == 'Yes' else 0
chest_pain_num = 1 if chest_pain == 'Yes' else 0

if st.button('Predict'):
    # Prepare the features for prediction
    features = np.array([gender_num, age, smoking_num, yellow_fingers_num, anxiety_num, peer_pressure_num,
                         chronic_disease_num, fatigue_num, allergy_num, wheezing_num,
                         alcohol_consuming_num, coughing_num, shortness_of_breath_num,
                         swallowing_difficulty_num, chest_pain_num])

    # Make prediction
    lung_cancer_prediction = predict_lung_cancer(features)

    # Display the result
    result = "Positive for Lung Cancer" if lung_cancer_prediction[0] == 1 else "Negative for Lung Cancer"
    st.write(f"Prediction: {result}")
