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
        return "(vertigo) Paroymsal  Positional Vertigo"
    elif prognosis == 1:
        return "AIDS"
    elif prognosis == 2:
         return "Acne"
    elif prognosis == 3: 
        return "Alcoholic hepatitis"
    elif prognosis == 4: 
        return "Allergy"
    elif prognosis == 5: 
        return "Arthritis"
    elif prognosis == 6: 
        return "Bronchial Asthma"
    elif prognosis == 7: 
        return "Cervical spondylosis"
    elif prognosis == 8: 
        return "Chicken pox"
    elif prognosis == 9: 
        return "Chronic cholestasis'
    elif prognosis == 10: 
        return "Common Cold"
    elif prognosis == 11: 
        return "Dengue"
    elif prognosis == 12: 
        return "Diabetes"
    elif prognosis == 13: 
        return "Dimorphic hemmorhoids(piles)"
    elif prognosis == 14: 
        return "Drug Reaction"
    elif prognosis == 15: 
        return "Fungal infection"
    elif prognosis == 16: 
        return "GERD"
    elif prognosis == 17: 
        return "Gastroenteritis"
    elif prognosis == 18: 
        return "Heart attack"
    elif prognosis == 19: 
        return "Hepatitis B"
    elif prognosis == 20: 
        return "Hepatitis C"
    elif prognosis == 21: 
        return "Hepatitis D"
    elif prognosis == 22: 
        return "Hepatitis E"
    elif prognosis == 23: 
        return "Hypertension "
    elif prognosis == 24: 
        return "Hyperthyroidism"
    elif prognosis == 25: 
        return "Hypoglycemia"
    elif prognosis == 26: 
        return "Hypothyroidism"
    elif prognosis == 27: 
        return "Impetigo"
    elif prognosis == 28: 
        return "Jaundice"
    elif prognosis == 29: 
        return "Malaria"
    elif prognosis == 30: 
        return "Migraine"
    elif prognosis == 31: 
        return "Osteoarthristis"
    elif prognosis == 32: 
        return "Paralysis (brain hemorrhage)"
    elif prognosis == 33: 
        return "Peptic ulcer diseae"
    elif prognosis == 34: 
        return "Pneumonia"
    elif prognosis == 35: 
        return "Psoriasis'
    elif prognosis == 36: 
        return "Tuberculosis"
    elif prognosis == 37: 
        return "Typhoid"
    elif prognosis == 38: 
        return "Urinary tract infection"
    elif prognosis == 39: 
        return "Varicose veins"
    elif prognosis == 40: 
        return "hepatitis A"

