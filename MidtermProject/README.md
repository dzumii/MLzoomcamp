# MLzoomcamp
Midterm Project
Dataset: 
Available on Kaggle at https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023/data?select=ds_salaries.csv

How to make predictions with the model
With linux:
$ gunicorn --bind=0.0.0.0:9696 predict:app
$ python predict-test.py

With docker:
$ docker build -t --rm midtermProject .
$ docker run -it --rm -p 9696:9696 midtermProject
$ gunicorn --bind=0.0.0.0:9696 predict:app

