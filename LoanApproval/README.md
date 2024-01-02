# MLzoomcamp
**Midterm Project**  
This projects predicts the outcome of a loan application based on certain features like age, experience, income, zip_code, family, ccavg, education, mortgage, securities_account, cd_account, online and creditcard.  

**Dataset:**  
Available on Kaggle at https://www.kaggle.com/datasets/vikramamin/bank-loan-approval-lr-dt-rf-and-auc 
How to make predictions with the model:  

Clone this repository  

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

