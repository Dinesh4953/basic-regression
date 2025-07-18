from flask import Flask, request, jsonify, render_template, redirect
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application


## Import ridge refressor and standard scalar
ridge_model = pickle.load(open('notebooks/ridge.pkl', 'rb'))
standard_scaler =pickle.load(open('notebooks/scaler.pkl', 'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        Temparature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_scaled_data = standard_scaler.transform([[Temparature, RH, Ws, Rain ,FFMC, DMC, ISI, Classes, Region]])
        result = ridge_model.predict(new_scaled_data)
        return render_template('home.html', results = result[0])
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run( debug=True)