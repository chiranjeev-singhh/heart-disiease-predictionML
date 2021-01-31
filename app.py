#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 22:27:06 2021

@author: chiranjeev
"""
import numpy as np
from flask import Flask, request, jsonify, render_template,flash, redirect,session, logging, url_for
import pickle
#from flask_login import current_user, login_required
#from flask_sqlalchemy import SQLAlchemy
#from forms import LoginForm, RegisterForm
#from werkzeug.security import generate_password_hash, check_password_hash
#from functools import wraps


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#app.config['SECRET_KEY'] = '!9m@S-dThyIlW[pHQbN^'

#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)

#class User(db.Model):

#    id = db.Column(db.Integer, primary_key=True)

#    name= db.Column(db.String(15), unique=True)

#    username = db.Column(db.String(15), unique=True)

#    email = db.Column(db.String(50), unique=True)

#    password = db.Column(db.String(256), unique=True)
@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.form['gender']=="Male":
        c=1
    else:
        c=0
    if request.form['chestpain']=="typical angina":
        a=0
    elif request.form['chestpain']=="atypical angina":
        a=1
    elif request.form['chestpain']=="non-anginal pain":
        a=2
    else:
        a=3
    if request.form['fb']=="Yes":
        b=0
    else:
        b=1
    if request.form['rest']=="normal":
        d=0
    else:
        d=1
    if request.form['exa']=="Yes":
        e=0
    else:
        e=1
    if request.form["slop"]=="upsloping":
        f=0
    elif request.form["slop"]=="flat":
        f=1
    else:
        f=2
    if request.form["tha"]=="normal":
        g=1
    elif request.form["tha"]=="fixed defect":
        g=2
    else:
        g=3
        go=['Age','trestbps','chol','thalch','oldpeak','ca']
    int_features =[int(request.form['Age']),c,a,int(request.form['trestbps']),int(request.form['chol']),b,d,int(request.form['thalch']),e,float(request.form['oldpeak']),f,int(request.form['ca']),g] 
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    if output==1:
        z="Chances of Heart Disease is More,Take Care"
    else:
        z="Hurray You Have less chances of Heart Disease,Stay Fit"

    return render_template('index.html', prediction_text=z)


if __name__ == "__main__":
    app.run(debug=True)

