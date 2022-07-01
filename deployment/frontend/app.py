import streamlit as st
import requests

st.title("Predict Churn")

Senior_format = {0:"not Senior Citizen",1:"Senior Citizen"}
def senior_format(option):
        return Senior_format[option]

tenure = st.number_input("tenure", min_value=1)
MonthlyCharges =st.number_input("MonthlyCharges", min_value=1)
TotalCharges=st.number_input("TotalCharges", min_value=1)
gender=st.selectbox("gender", ['Male', 'Female'])
SeniorCitizen = st.selectbox("SeniorCitizen", options=list(Senior_format.keys()),format_func=senior_format)
Partner = st.radio("Partner", ['No', 'Yes'])
Dependents= st.radio("Dependents", ['No', 'Yes'])
PhoneService= st.radio("PhoneService", ['No', 'Yes'])
MultipleLines= st.radio("MultipleLines", ['No phone service','No', 'Yes'])
InternetService= st.radio("InternetService", ['DSL','Fiber optic','No'])
OnlineSecurity= st.radio("OnlineSecurity", ['No', 'Yes', 'No internet service'])
OnlineBackup= st.radio("OnlineBackup", ['No', 'Yes', 'No internet service'])
DeviceProtection= st.radio("DeviceProtection", ['No', 'Yes', 'No internet service'])
TechSupport= st.radio("TechSupport", ['No', 'Yes', 'No internet service'])
StreamingTV= st.radio("StreamingTV", ['No', 'Yes', 'No internet service'])
StreamingMovies= st.radio("StreamingMovies", ['No', 'Yes', 'No internet service'])

Contract=st.radio("Contract", ['Month-to-month', 'One year', 'Two year'])

PaperlessBilling= st.radio("PaperlessBilling", ['No', 'Yes'])
PaymentMethod= st.radio("PaymentMethod", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])

# inference
data = {'tenure':tenure,
        'MonthlyCharges':MonthlyCharges,
        'TotalCharges':TotalCharges,
        'gender': gender,
        'SeniorCitizen':SeniorCitizen,
        'Partner':Partner, 
        'Dependents':Dependents,
        'PhoneService':PhoneService,
        'MultipleLines' : MultipleLines,
        'InternetService' : InternetService,
        'OnlineSecurity' : OnlineSecurity,
        'OnlineBackup' : OnlineBackup,
        'DeviceProtection' : DeviceProtection,
        'TechSupport' : TechSupport,
        'StreamingTV' : StreamingTV,
        'StreamingMovies' : StreamingMovies,
        'Contract' : Contract,
        'PaperlessBilling' : PaperlessBilling,
        'PaymentMethod' : PaymentMethod}
        

URL = "https://austin-deployment-backend-p2m1.herokuapp.com/predict"

# komunikasi
if st.button('Predict'):
        r = requests.post(URL, json=data)
        res = r.json()
        if res['code'] == 200:
                st.title(res['result']['classes'])

