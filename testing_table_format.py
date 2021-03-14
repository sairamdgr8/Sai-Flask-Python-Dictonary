# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:49:02 2021

@author: Bunnyyyyyyy
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 22:23:08 2021

@author: Bunnyyyyyyy
"""

from flask import Flask, render_template, request
import requests
import numpy as np
from PyDictionary import PyDictionary
from tabulate import tabulate
import pandas as pd

df = pd.DataFrame({'Noun': ['something that is likely to vary; something that is subject to variation', 'a quantity that can assume any of a set of values', 'a star that varies noticeably in brightness', 'a symbol (like x or y'], 'Adjective': ['liable to or capable of change', 'marked by diversity or difference', '(used of a device', 'as e.g. light']})
print(tabulate(df, headers='keys', tablefmt='psql',showindex=False))

app = Flask(__name__)


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        myword = request.form['myword']
        prediction=PyDictionary.meaning(myword)
        output=prediction
        if(output!=None):
            df = pd.DataFrame.from_dict(output, orient='index')
            df=df.transpose()
            return render_template('index.html',prediction_text="the following meanings  for the word \n :"+ myword + tabulate(df, headers='keys', tablefmt='psql',showindex=False))
          
        else:
            return render_template('index.html',prediction_text="There is no specific meaning to this Word \n:"+ myword )

            

if __name__=="__main__":
    app.run()