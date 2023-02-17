# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 16:45:02 2022

@author: Lenovo
"""
from flask import Flask,jsonify
import requests
app = Flask(__name__)
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/astros.json",
                        params=parameters)
data = response.json()



@app.route('/number')
def number():
    return "Number of people: {}".format(data['number'])

@app.route('/name')
def name_craft():
    return jsonify(data['people'])



if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=False)