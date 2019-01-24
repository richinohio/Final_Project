from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.backend import clear_session
import matplotlib.pyplot as plt
import pandas as pd
import os
import warnings
warnings.simplefilter('ignore')
import numpy as np
import pickle


def prediction_lin(Property_Code1, p2,p3,p4, Bedrooms, Bathrooms,SQFT):

    #import pickled model
    trained_model_lin = pickle.load(open('models/linear_model.pkl','rb'))

    # Make prediction from the loaded model
    predict_lin = trained_model_lin.predict([[Property_Code1,p2,p3,p4,Bedrooms,Bathrooms,SQFT]])
    #result_lin="${:,.2f}".format(predict_lin)
    return predict_lin


def prediction_log(Property_Code1, p2,p3,p4, Bedrooms, Bathrooms,SQFT,Rent):
    #import pickled model    
    list_pickle = open('models/logisitic_depp_network.pkl','rb') 
    trained_model_log = pickle.load(list_pickle)

    # Make prediction from the loaded model
    predict_log = trained_model_log.predict_classes([[[SQFT,Bedrooms,Bathrooms,Rent,Property_Code1, p2,p3,p4]]])
    clear_session()
    return predict_log