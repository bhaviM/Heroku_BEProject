# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:07:38 2019

@author: LENOVO
"""

import requests
import json
url = 'http://localhost:5000/api'
data={'Gender':'0','Age':'0','RS':'1'}
headers={'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.status_code)   #prints status code
print(r.text)
#print(r.json())
