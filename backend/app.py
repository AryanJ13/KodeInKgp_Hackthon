from flask import Flask, request, jsonify
import user.py

app = Flask(__name__)


@app.route("/", methods=["POST"])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user", methods=["POST"])
def testpost():
     input_json = request.get_json(force=True) 
     dictToReturn = {
        'text': ,
        '':
        }
     return jsonify(dictToReturn)    
