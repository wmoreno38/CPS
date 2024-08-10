# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:01:48 2024

@author: yxg084228
"""

from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Cargar el modelo entrenado
with open('titanic_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Definir el orden de las columnas
expected_columns = ['Pclass', 'Age', 'SibSp', 'Parch']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame(data)
    # Asegurarse de que las columnas estén en el orden correcto
    df = df[expected_columns]
    predictions = model.predict(df)
    return jsonify(predictions.tolist())

@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    data = request.json
    df = pd.DataFrame(data)
    # Asegurarse de que las columnas estén en el orden correcto
    df = df[expected_columns]
    predictions = model.predict(df)
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
