# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 12:58:26 2019

@author: LENOVO
"""

from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def handle_data():
    gender=request.args.get('gender')
    return "The gender is :{} ".format(gender)

if __name__ == '__main__':
    app.run()