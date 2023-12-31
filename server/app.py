# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:34:28 2023

@author: Tanvir Ahmed
"""

import sklearn
import json
import pickle
import numpy as np
from flask import Flask,request,jsonify

__data_columns = None
__locations = None
__model = None

def get_estimated_price(location,total_sqft,bath,balcony,bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
        
    m = np.zeros(len(__data_columns))
    m[0] = total_sqft
    m[1] = bath
    m[2] = balcony
    m[3] = bhk
    if loc_index >= 0:
        m[loc_index] = 1
    return round(__model.predict([m])[0],2)

def get_locations_names():
    return __locations

def load_save_artifacts():
    print("Loding Save artifacts...Starts")
    
    global __data_columns
    global __locations
    with open("./artifacts/columns.json","r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[4:]

    global __model
    with open("./artifacts/home_prices_model.pickle","rb") as f:
        __model = pickle.load(f)

    print("Loading Saved artifacts..Ends")

app = Flask(__name__)

@app.route("/get_locations_names")
def get_locations_names_route():
    response = jsonify({
        "locations":get_locations_names()
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/predict_home_price",methods=["POST"])
def predict_home_price():
    location = request.form['location']
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])
    bhk = int(request.form['bhk'])
    response = jsonify({
        "estimated_price":get_estimated_price(location,total_sqft,bath,balcony,bhk)
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

if __name__ == "__main__":
    load_save_artifacts()
    print(get_locations_names())
    print(get_estimated_price("1st Block Jayanagar",1056,2,1,2))
    print(get_estimated_price('shivaji nagar',1000,2,2,2))
    app.run()