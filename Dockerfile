FROM python:3.11.2-slim-buster

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY ml/lstm_model.h5 /app/ml/lstm_model.h5

COPY data/comsumption.csv /app/data/comsumption.csv

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]