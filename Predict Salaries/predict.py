#!/usr/bin/env python
# coding: utf-8

import pickle
import xgboost as xgb
import numpy as np

from flask import Flask
from flask import request
from flask import jsonify

model_file = "SalariesModel.bin"

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('Salaries')

@app.route('/predict', methods=['POST'])
def predict():
    data_prefessional = request.get_json()

    data_prefessional_data = dv.transform([data_prefessional])
    features = list(dv.get_feature_names_out())
    X = xgb.DMatrix(data_prefessional_data,feature_names=features)
    y_pred = model.predict(X)
    salary_pred = np.expm1(y_pred)
    

    result = {
        'Salary': float(salary_pred),
        
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

