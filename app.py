import os
import numpy as numpy
import flask
import pickle
from flask import Flask, render_template, request

#creating instances of the class
app=Flask(__name__)

#to tell flask what url should trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

#prediction function
def VacantPredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,12)
    loaded_model = pickle.load(open("model.pkl"))
    return result[0]

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = VacantPredictor(to_predict_list)

        if int(result)==1:
            prediction = 'occupied'
        
        else:
            prediction = 'vacant'

    return render_template("result.html",prediction=prediction)