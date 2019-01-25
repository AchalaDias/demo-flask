import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    'mongodb://datastore:27017/dockerdemo')
db = client.tododb


@app.route('/')
def todo():

    _items = db.tododb.find()
    items = [item for item in _items]
    
    return { items }, 200


@app.route('/new', methods=['POST'])
def new():

    item_doc = {
        'name': request.json['name']
    }
    db.tododb.insert_one(item_doc)

    return item_doc, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)