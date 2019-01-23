from flask import Flask, render_template, request, session, g, redirect, url_for, abort, \
     render_template, flash
import os
from predict import prediction_lin

import sys
app1 = Flask(__name__)

@app1.route('/', methods=['GET'])
def mainpage():
    return render_template('index_lin.html')

@app1.route('/',methods=['POST'])
def posst():
    att1 = int(request.form['Property_Code'])
    if att1 == 0:
        apt1 =1
        apt2 =0
        apt3 =0
        apt4 =0
    elif att1 ==1:
        apt1 =0
        apt2 =1
        apt3 =0
        apt4 =0
    elif att1 ==2:
        apt1 =0
        apt2 =0
        apt3 =1
        apt4 =0
    elif att1 ==3:
        apt1 =0
        apt2 =0
        apt3 =0
        apt4 =1
    att2 = int(request.form['Bedrooms'])
    att3 = int(request.form['Bathrooms'])
    att4 = int(request.form['SQFT'])
    if att4 == 0:
        sqft = 500
    elif att4 == 1:
        sqft = 600
    elif att4 == 2:
        sqft = 700
    elif att4 == 3:
        sqft = 800
    elif att4 == 4:
        sqft = 900
    print(att4, file=sys.stderr)
    #predictive function using model.prediction
    rent_pred = prediction_lin(apt1,apt2,apt3,apt4,att2,att3,sqft)
    return render_template('result_lin.html', result=rent_pred),att2

"""
app2 = Flask(__name__)

@app2.route('/', methods=['GET'])
def mainpage():
    return render_template('index_log.html')

@app2.route('/',methods=['POST'])
def print():
    att1 = request.form['Property_Code']
    att2 = request.form['BedRooms']
    att3 = request.form['Bathroom']
    att4 = request.form['SQFT']
    att5 = request.form['chrent']
    
    #predictive function using model.prediction
    vacancy_pred = prediction_log(att1,att2,att3,att4,att5)
    return render_template('result_log.html', result=LOS_pred)
"""

if __name__ == '__main__':
    app1.run(port=5000, debug=True)   