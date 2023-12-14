#!/usr/bin/env python
# coding: utf-8

import requests

url = 'http://localhost:9696/predict'

data_prefessional_id = 'xyz-123'
data_prefessional = {
"work_year": 2020,
"experience_level":"EN",
"employment_type":"CT",
"job_title   ":"Finance Data Analyst",
"salary_currency ":"MXN",
"salary_in_usd  ": 1000,
"employee_residence " :"MT",
"remote_ratio  " :50,
"company_location " :"MT",
"company_size  ":"S"
}

response = requests.post(url, json=data_prefessional).json()
print(response)


# response = requests.post(url, json=data_prefessional)
# print(response.content)
