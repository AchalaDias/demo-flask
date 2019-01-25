FROM python:2.7

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=app.py

CMD flask run 