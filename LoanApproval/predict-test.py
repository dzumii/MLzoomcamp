#!/usr/bin/env python
# coding: utf-8
import json
import requests

url = 'http://localhost:9696/predict'

loan_applicant_id = 'xyz-123'
loan_applicant = {
    'age': 30,
    'experience': 10,
    'income': 100,
    'zip_code': 91107,
    'family': 5,
    'ccavg': 0.5,
    'education': 3,
    'mortgage': 20,
    'securities_account': 1,
    'cd_account': 0,
    'online': 0,
    'creditcard': 1
}


try:
    response = requests.post(url, json=loan_applicant)
    # Print response status code
    print(f"Response Status Code: {response.status_code}")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Load JSON and print with indentation
        result = json.loads(response.content)
        print("Prediction Result:")
        print(json.dumps(result, indent=2))
    else:
        print("Error:")
        print(response.text)

except Exception as e:
    print(f"An error occurred: {e}")