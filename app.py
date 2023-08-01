from db import Database
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
db = Database('notas.db')

@app.route('/')
def hello_world():
    return


@app.route('/notes',methods=['GET'])
def shownotes():
    notes = db.fetch()
    return jsonify(notes)

@app.route('/notes',methods=['POST'])
def add_notes():
    data = request.get_json()
    title = data.get('title')
    body = data.get('body')
    db.insert(title,body)
    return jsonify({"message":"Nota adcionada com sucesso"})

    
#@app.route('remove/<id>',methods=['POST'])
#def remove(<id>):
    #db.remove(id)
    #return jsonify({"message": "Nota removida com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)
