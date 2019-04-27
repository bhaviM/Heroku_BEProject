# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:53:57 2019

@author: LENOVO
"""

import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/api',methods=['GET','POST'])
def predict():
    data=request.get_json()
   # res=dict()
    
    #for key in data.keys():
       # res[key]=model.predict(np.array(data))
        
    # Make prediction using model loaded from disk as per the data.
    
    #prediction=model.predict([[np.array(data['Gender','Age','RS'])]])
    #prediction=model.predict(np.array(data['Gender','Age','RS']))

    # Take the first value of prediction
    #output=prediction[0]
    #return jsonify(output)
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
