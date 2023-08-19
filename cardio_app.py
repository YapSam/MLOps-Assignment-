from flask import Flask,request, url_for, redirect, render_template, jsonify
from pycaret.classification import *
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = load_model('model_classifier_cardio')
cols = ['age', 'gender', 'chest_pain', 'resting_BP', 'cholesterol',
       'fasting_BS', 'resting_ECG', 'max_HR', 'exercise_angina', 'old_peak',
       'ST_slope']

@app.route('/')
def home():
    return render_template("cardio_home.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(model, data=data_unseen)
    prediction = int(prediction.prediction_label)
    return render_template('cardio_home.html',pred='Cardiovascular Disease status of {} [0:No, 1:Present]'.format(prediction))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = predict_model(model, data=data_unseen)
    output = prediction.Label[0]
    return jsonify(output)

if __name__ == '__main__':
    # app.debug = True 
    app.run(host='0.0.0.0', port=5000)
