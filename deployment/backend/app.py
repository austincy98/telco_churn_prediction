from distutils.log import debug
from flask import Flask, jsonify, request
import numpy as np
import pickle
import pandas as pd
import tensorflow as tf

app = Flask(__name__)


LABEL = ['No', 'Yes']
columns=['tenure','MonthlyCharges','TotalCharges','gender', 'SeniorCitizen', 'Partner', 'Dependents',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']
       
with open("preprocessing.pkl", "rb") as f:
    pipe_pre = pickle.load(f)

model=tf.keras.models.load_model("model_sequential.h5")

@app.route("/")
def homepage():
    return "<h1>Backend Pemodelan Churn </h1>"

@app.route("/predict", methods=["GET", "POST"])
def diabetes_inference_ada():
    if request.method == 'POST':
        data = request.json
        print(data)
        new_data = [data['tenure'],
                        data['MonthlyCharges'],
                        data['TotalCharges'],
                        data['gender'],
                        data['SeniorCitizen'],
                        data['Partner'],
                        data['Dependents'],
                        data['PhoneService'],
                        data['MultipleLines'],
                        data['InternetService'],
                        data['OnlineSecurity'],
                        data['OnlineBackup'],
                        data['DeviceProtection'],
                        data['TechSupport'],
                        data['StreamingTV'],
                        data['StreamingMovies'],
                        data['Contract'],
                        data['PaperlessBilling'],
                        data['PaymentMethod']]

        new_data = pd.DataFrame([new_data],columns=columns)

        new_data_preprocessed = pipe_pre.transform(new_data)

        result=model.predict(new_data_preprocessed)
        res = np.where(result >= 0.5, 1, 0)
        print("res :", res )
        response = {'code':200, 'status':'OK',
                    'result':{'prediction': str(res[0]),
                              'classes': LABEL[int(res[0])]}}


        return jsonify(response)
            

    return "Silahkan gunakan method post untuk mengakses model"

