import json
import pickle
import os
import numpy as np

# Global Variables
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath,ready_to_move):
    # All our location in columns.json are lower so the inputed location also have to be lower case
    # __data_columns is a list and to find an index in a list just use the method .index
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = ready_to_move
    x[3] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    
    # This method will return a 2D array and the first position is the prediction number as an float number
    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    # i'm having problems with the location so i will do this 
    with open(os.getcwd() +  "/server/artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        # Using slicing to get the locations
        __locations = __data_columns[4:]

    with open(os.getcwd() +  "/server/artifacts/banglore_home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3, 1))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2, 0))
    print(get_estimated_price('Kalhalli', 1000, 2, 2, 1))
    # Other Location Test
    print(get_estimated_price('Centro', 1000, 2, 2, 0))