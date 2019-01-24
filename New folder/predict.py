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
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import os
import warnings
warnings.simplefilter('ignore')
import numpy as np
import pickle


#def prediction_lin(Property_Code, Bedrooms, Bathrooms,SQFT):
def prediction_lin(Property_Code1, p2,p3,p4, Bedrooms, Bathrooms,SQFT):
    # Create of row of data that comabines all user inputs
    #title_lin={"Property_Code":[Property_Code], "Bedrooms":[Bedrooms], "Bathrooms":[Bathrooms],"SQFT":[SQFT]}
    #test_lin = pd.DataFrame(title_lin)

    #import pickled model
    trained_model_lin = pickle.load(open('models/linear_model.pkl','rb'))

    # Make prediction from the loaded random forest model
    predict_lin = trained_model_lin.predict([[Property_Code1,p2,p3,p4,Bedrooms,1,SQFT]])
    #result_lin="${:,.2f}".format(predict_lin)
    return predict_lin
def prediction_log(Property_Code1, p2,p3,p4, Bedrooms, Bathrooms,SQFT,Rent):
    list_pickle = open('models/logisitic_depp_network.pkl','rb') 
    trained_model_log = pickle.load(list_pickle)
    #predict_log = trained_model_log.predict_classes([[[SQFT,Bedrooms,Bathrooms,Rent,Property_Code1, p2,p3,p4]]])
    predict_log = trained_model_log.predict_classes([[[SQFT,Bedrooms,Bathrooms,Rent,Property_Code1, p2,p3,p4]]])
    clear_session()
    return predict_log
"""
def prediction_log(Property_Code, BedRooms, Bathroom,SQFT, chrent):
    
    # Create of row of data that comabines all user inputs
    title_log={"Property_Code":[Property_Code], "BedRooms":[BedRooms], "Bathroom":[Bathroom],"SQFT":[SQFT],"chrent":[chrent]}
    test_log = pd.DataFrame(title_log)

    #import pickled model
    trained_model_log = pickle.load(open('logistic_deep_model.pkl','rb'))

    # Make prediction from the loaded random forest model
    predict_log = trained_model_log.predict(test_log)[0]
    result_log="${:,.2f}".format(predict_log)
    return result_log
"""