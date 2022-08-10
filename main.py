from crypt import methods
from flask import Flask, jsonify
from view_records import *

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Endpoint for "Show Records"
@app.route('/empdetails', methods=['GET'])
def Showrecords():
    return jsonify(recordsList)

# Endpoint for "Addition"
@app.route('/tenplus/<int:a>')
def sum(a):
    result =  {
        "First No" : 10,
        "Second No" : a,
        "Answer" : str(10 + a)
    }
    return jsonify(result)

# Endpoint for "Substraction"
@app.route('/tenminus/<int:b>')
def avg(b):
    result =  {
        "First No" : 10,
        "Second No" : b,
        "Answer" : str(10 - b)
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)