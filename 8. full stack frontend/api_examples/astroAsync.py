# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 16:45:02 2022

@author: Lenovo
https://geekyhumans.com/create-asynchronous-api-in-python-and-flask/
"""
import threading
import asyncio
from flask import Flask,jsonify, render_template
import requests

import json 
app = Flask(__name__)
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/astros.json",
                        params=parameters)
data = response.json()

@app.route('/0')
def home():
   return render_template('home.html')

@app.route('/1')
def astro():
   return render_template('astro.html')
#   return render_template('astro.html',jsonfile=jsonify(data['people']))

@app.route('/read')
def readfile():
   return render_template('xxreadfile.html')

@app.route('/pic')
def getPic():
   return render_template('getPic.html')

@app.route('/number')
def number():
    return "Number of people: {}".format(data['number'])

@app.route('/name')
def name_craft():
    return jsonify(data['people'])



if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=False)