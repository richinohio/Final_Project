from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import pandas as pd
import os
import warnings
warnings.simplefilter('ignore')
import numpy as np
import pickle

def prediction(OverallQual, GrLivArea, GarageCars,YearBuilt,FullBath):
    
    # Create of row of data that comabines all user inputs
    title={"OverallQual":[OverallQual], "GrLivArea":[GrLivArea], "GarageCars":[GarageCars],"YearBuilt":[YearBuilt],"FullBath":[FullBath]}
    test = pd.DataFrame(title)

    #import pickled model
    trained_model = joblib.load('model.pkl')

    # Make prediction from the loaded random forest model
    predict = trained_model.predict(test)[0]
    result="${:,.2f}".format(predict)
    return result

def prediction(OverallQual, GrLivArea, GarageCars,YearBuilt,FullBath):
    
    # Create of row of data that comabines all user inputs
    title={"OverallQual":[OverallQual], "GrLivArea":[GrLivArea], "GarageCars":[GarageCars],"YearBuilt":[YearBuilt],"FullBath":[FullBath]}
    test = pd.DataFrame(title)

    #import pickled model
    trained_model = joblib.load('model.pkl')

    # Make prediction from the loaded random forest model
    predict = trained_model.predict(test)[0]
    result="${:,.2f}".format(predict)
    return result