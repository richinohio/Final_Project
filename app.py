from flask import Flask, render_template, request, session, g, redirect, url_for, abort, \
     render_template, flash
import os
from predict import prediction_log, prediction_lin

app1 = Flask(__name__)

@app1.route('/', methods=['GET'])
def mainpage():
    return render_template('index.html')

@app1.route('/',methods=['POST'])
def print():
    att1 = request.form['Property_Code']
    att2 = request.form['BedRooms']
    att3 = request.form['Bathroom']
    att4 = request.form['SQFT']

#predictive function using model.prediction
rent_pred = prediction_lin(att1,att2,att3,att4)

return render_template('result_lin.html', result=rent_pred)

app2 = Flask(__name__)

@app2.route('/', methods=['GET'])
def mainpage():
    return render_template('index.html')

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

if __name__ == '__main__':
    app1.run(port=5000, debug=True)
    app2.run(port=8000, debug=True)



