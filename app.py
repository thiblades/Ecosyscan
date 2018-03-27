#! /usr/local/bin/python3
from flask import Flask
from flask import request
from flask import render_template

import requests
import csv
import json

# Function to retrieve the stock prices from the API
BASE = 'json.json'

def getJsonData():
	with open(BASE) as json_data:
		d = json.load(json_data)
		print(d)
		return d
	

# Declare the Flask application
app = Flask("BigSmoke")

# index route, the page that displays the stock prices
@app.route('/', methods=['GET'])
def index_page():
	
	# Fetch the price data and serve a page containing it.
	data = getJsonData()
	
	return render_template('index.html', 
		data=data
	)

# Run the server
app.run(host='localhost', port=7777)

