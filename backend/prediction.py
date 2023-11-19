import pickle
import pandas as pd
import json

def predict_disease(config):
    ##loading the model from the saved file
    pkl_filename = "model.pkl"
    with open(pkl_filename, 'rb') as f_in:
        model = pickle.load(f_in)

    if type(config) == dict:
        df = pd.DataFrame(config)
    else:
        df = config
    
    prognosis = model.predict(df)
    
    if prognosis == 0:
        return "Test1"
    elif prognosis == 1:
        return "Test2"
    if prognosis == 2:
        return "Test3"