from flask import Flask, render_template, request, session, g, redirect, url_for, abort, \
     render_template, flash
import os
from predict import prediction_lin

import sys
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('cover.html')

@app.route('/linear', methods=['GET'])
def linindex():
    return render_template('index_lin.html')

@app.route('/linear', methods=['POST'])
def linfunc():
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
    att3 = float(request.form['Bathrooms'])
    att4 = int(request.form['SQFT'])
  
    #predictive function using model.prediction
    rent_pred = prediction_lin(apt1,apt2,apt3,apt4,att2,att3,att4)
    return render_template('result_lin.html', result=rent_pred)

@app.route('/logistic', methods=['GET'])
def logindex():
    return render_template('index_log.html')

@app.route('/logistic',methods=['POST'])
def logfunc():
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
    att2 = int(request.form['BedRooms'])
    att3 = float(request.form['Bathrooms'])
    att4 = int(request.form['SQFT'])
    att5 = int(request.form['exampleInputAmount'])
'''
    #predictive function using model.prediction
    vac_pred = prediction_log(apt1,apt2,apt3,apt4,att2,att3,att4)
    return render_template('result_lin.html', result=vac_pred)
'''
if __name__ == '__main__':
    app.run(port=5000, debug=True)   