import pickle
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense , Dropout

pkl_filename = "model.pkl"
with open(pkl_filename, 'rb') as f_in:
    model = pickle.load(f_in)

# Example model architecture
model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(32, activation='relu'),
    Dropout(0.5),
    Dense(16, activation='relu'),
    Dropout(0.3),
    Dense(1, activation='sigmoid')
])

# Print summary of the model
model.summary()

# Assuming you have a trained model named 'model'
import numpy as np


input_data = np.random.rand(10).reshape(1, 10)  

# Make predictions
predictions = model.predict(input_data)

# Display predictions
print(predictions)

