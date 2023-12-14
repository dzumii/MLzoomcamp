# MLzoomcamp
**Midterm Project**  
This projects predicts salary of a data professional due to certain features like work_year, experience_level, employment_type, job_title, salary_currency, salary_in_usd, employee_residence, remote_ratio,company_location and company_size.  

**Dataset:**  
Available on Kaggle at https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023/data?select=ds_salaries.csv  
How to make predictions with the model:  

Clone this repository  

Change your working directory to the Predict_Salaries directory  

Use pipenv to install the dependencies from the pipfile
```
pip install pipenv
```
Activate the new virtual environment  
```
pipenv install
```

**Locally without Docker:** 
```
pipenv run gunicorn --bind=0.0.0.0:9696 predict:app
```
``` 
pipenv run python predict-test.py
```  

**Locally with Docker:**  
Build the docker image  
```
docker build -t project .
```
Run the docker image  
``` 
docker run -it --rm -p 9696:9696 project
```
Predict:  
```  
pipenv run python predict-test.py
```

