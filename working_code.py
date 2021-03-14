# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 22:23:08 2021

@author: Bunnyyyyyyy
"""

from flask import Flask, render_template, request
import requests
import numpy as np
from PyDictionary import PyDictionary
app = Flask(__name__)


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        myword = request.form['myword']
        prediction=PyDictionary.meaning(myword)
        output=prediction
        if(output!=None):
            return render_template('index.html',prediction_text="the following meanings  for the word :"+ myword +" "+str(output))
        else:
            return render_template('index.html',prediction_text="There is no specific meaning to this Word :"+ myword )

            

if __name__=="__main__":
    app.run()

