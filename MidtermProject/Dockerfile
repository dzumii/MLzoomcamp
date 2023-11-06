FROM python:3.8.12-slim

RUN pip install pipenv
RUN pip install numpy
RUN pip install scipy
RUN pip install xgboost==2.0.0
RUN pip install scikit-learn==1.3.1

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "../"]

RUN pipenv install --system --deploy

COPY ["predict.py", "SalariesModel.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]