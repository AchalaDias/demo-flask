FROM python:2.7

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASK_APP=run.py

CMD flask run 