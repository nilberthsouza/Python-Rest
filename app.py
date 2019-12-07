from db import Database
import json
from flask import Flask

app = Flask(__name__)
db = Database('notas.db')

@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/notes',methods=['GET'])
def shownotes():
    not
