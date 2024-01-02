#!/usr/bin/env python
# coding: utf-8

import pickle
import json
import numpy as np

from flask import Flask
from flask import request
from flask import jsonify

model_file = "LoanModel.bin"

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('Loan')

@app.route('/predict', methods=['POST'])
def predict():
    loan_applicant = request.get_json()

    X = dv.transform([loan_applicant])
    y_pred = model.predict(X)
   
    result = {
        'Loan Status': y_pred.tolist(),
        
    }

    return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)