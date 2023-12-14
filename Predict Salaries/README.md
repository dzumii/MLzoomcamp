# MLzoomcamp
**Midterm Project** 
**Dataset:**  
Available on Kaggle at https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023/data?select=ds_salaries.csv  
How to make predictions with the model:  

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

**Locally without Docker:**  
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

