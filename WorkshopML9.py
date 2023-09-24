import streamlit as st
import json
import requests

# Streamlit UI
st.title("Azure ML Prediction")

# Input form
st.write("Enter Patient Data:")
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=0, max_value=120, value=0)
hypertension = st.checkbox("Hypertension")
heart_disease = st.checkbox("Heart Disease")
ever_married = st.checkbox("Ever Married")
work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "Children", "Never_worked"])
residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0, value=0.0)
bmi = st.number_input("BMI", min_value=0.0, value=0.0)
smoking_status = st.selectbox("Smoking Status", ["formerly smoked", "never smoked", "smokes", "Unknown"])

if st.button("Predict"):
    # Prepare data
    data = {
        "Inputs": {
            "data": [
                {
                    "id": 0,
                    "gender": gender,
                    "age": age,
                    "hypertension": 1 if hypertension else 0,
                    "heart_disease": 1 if heart_disease else 0,
                    "ever_married": ever_married,
                    "work_type": work_type,
                    "Residence_type": residence_type,
                    "avg_glucose_level": avg_glucose_level,
                    "bmi": bmi,
                    "smoking_status": smoking_status
                }
            ]
        },
        "GlobalParameters": {
            "method": "predict"
        }
    }

    # Send request to Azure ML service
    url = 'http://de14b654-7d55-4da4-a62b-ec578a43c232.southeastasia.azurecontainer.io/score'
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            result = response.json()
            st.write("Prediction Result:", result)
        else:
            st.error(f"Prediction failed with status code: {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
