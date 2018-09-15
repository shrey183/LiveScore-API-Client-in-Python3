#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 01:48:18 2018

@author: shrey.aryan
"""

import urllib.request
import json
import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

# In case the key and secret need to be modified
key = '6r94GgdPiJ5ciqdx'
secret = '70Qx0KjZN2uD6jfdLohrFuhXem9wNm4U'
# To get tomorrow's fixture
tomorrow = str(datetime.date.today() + datetime.timedelta(days = 1))


@app.route("/")
def home():
    return render_template('home.html')


# Task 1: Show all livescores.
@app.route("/all-livescores")
def all_livescores():
    htmlfile = urllib.request.urlopen("http://livescore-api.com/api-client/scores/live.json?key=" + key + "&secret=" + secret)
    json_data = htmlfile.read().decode('utf-8')
    dic = json.loads(json_data)['data']['match']
    return render_template('all-livescores.html',data = dic)



# Task 2: Show all livescores for a particular country if the country id is known.
@app.route("/livescoresCountry",methods=['POST']) 
def c_scores():
    cid = request.form['cid']
    htmlfile = urllib.request.urlopen("http://livescore-api.com/api-client/scores/live.json?key=" + key + "&secret=" + secret + "&country=" + cid)
    json_data = htmlfile.read().decode('utf-8')
    dic = json.loads(json_data)['data']['match']
    return render_template('livescoresCountry.html',data = dic)



# Task 3: Show fixtures tomorrow.
@app.route('/fixtures-tomorrow')
def fix_tom():
    htmlfile = urllib.request.urlopen("http://livescore-api.com/api-client/fixtures/matches.json?key=" + key + "&secret=" + secret+"&date=" + tomorrow)
    json_data = htmlfile.read().decode('utf-8')
    dic = json.loads(json_data)['data']['fixtures']
    return render_template('fixtures-tomorrow.html',data = dic)
    

if __name__ == '__main__':
    app.run(debug=True)
