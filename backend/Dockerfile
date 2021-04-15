FROM python:3
 
ENV PYTHONUNBUFFERE 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt ./app/requirements.txt

RUN pip install -r requirements.txt

RUN newrelic-admin generate-config 08043b5e698036ed0ec0ca11abdb010333e6NRAL newrelic.ini

COPY . /app