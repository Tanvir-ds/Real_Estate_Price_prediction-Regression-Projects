import sklearn
import json
import pickle
import numpy as np

__data_columns = None
__locations = None
__model = None

def get_estimated_price(location, total_sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    m = np.zeros(len(__data_columns))
    m[0] = total_sqft
    m[1] = bath
    m[2] = bhk
    if loc_index >= 0:
        m[loc_index] = 1
    return round(__model.predict([m])[0], 2)

def get_locations_names():
    return __locations

def load_save_artifacts():
    print("Loading Saved artifacts...Starts")

    global __data_columns
    global __locations
    with open("./columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[4:]

    global __model
    with open("./home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("Loading Saved artifacts...Ends")

if __name__ == "__main__":
    load_save_artifacts()
    print(get_locations_names())
    print(get_estimated_price("1st Block Jayanagar", 1056, 2, 2))
    print(get_estimated_price("1st Block Jayanagar", 1056, 2, 3))
    print(get_estimated_price("shivaji nagar", 1000, 2, 2))
    print(get_estimated_price("shivaji nagar", 1000, 2, 3))
