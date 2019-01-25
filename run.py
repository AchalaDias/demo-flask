from flask_api import FlaskAPI
from flask_restful import Api
from flask_cors import CORS
import os
from redis import Redis
from flask import Flask, request, jsonify

redis = Redis(host="redis", db=0, socket_timeout=5, charset="utf-8", decode_responses=True)

app = FlaskAPI(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return {'version': 'version 1.0.0'}, 200

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        name = request.json['name']
        redis.rpush('students', {'name': name})
        return jsonify({'name': name})

    if request.method == 'GET':
        return jsonify(redis.lrange('students', 0, -1))


app.debug = True
host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', 5000))
app.run(host=host, port=port)

