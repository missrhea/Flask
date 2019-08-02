# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle


def predict_value(test_X):
    x = test_X
    x = np.array(int(x))
    x = x.reshape(1,-1)
    
    regressor = pickle.load(open('pickled-model', 'rb'))
    
    prediction = regressor.predict(x)
    
    #print(prediction)
    
    return (prediction)

