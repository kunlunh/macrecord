from flask import Flask
from flask import render_template
from flask import request,jsonify
import macrecord
from macrecord import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getrecord', methods=['GET', 'POST'])
def getrecord():
	res = getrecordfromfile()
	
	return jsonify(res)

@app.route('/setrecord', methods=['GET', 'POST'])
def setrecord():
	dataform = request.get_data()
	setrecordtofile(dataform)
	res = "111"
	return jsonify(res)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8011)