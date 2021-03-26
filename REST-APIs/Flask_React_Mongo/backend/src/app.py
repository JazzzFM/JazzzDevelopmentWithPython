# !/usr/bin/env python
# encoding: utf-8
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)


@app.route('/users', methods = ['POST'])
def createUsers():
    return 'received'

@app.route('/users', methods = ['POST'])
def getUsers():
    return 'received'

@app.route('/users/<id>', methods = ['POST'])
def getUser():
    return 'received'

@app.route('/users/<id>', methods = ['POST'])
def createUser():
    return 'received'

@app.route('/users/<id>', methods = ['POST'])
def deleteUser():
    return 'received'

@app.route('/users/<id>', methods = ['PUT'])
def updateUser():
    return 'received'

if __name__ == "__main__":
    app.run(debug=True)
