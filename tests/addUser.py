#!/usr/bin/python

import requests, json
import sys

try:
    if len(sys.argv[1]) > 0:
        username = sys.argv[1]
except IndexError:
    username = 'user'
username = ''
try:
    if len(sys.argv[2]) > 0:
        ip = sys.argv[2]
except IndexError:
    ip = "172.16.78.135:8000"
    
url = "http://" + ip + "/poker/user/";
payload = json.dumps({'username':username}) 

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

print "Posting to " + url + " with payload " + payload
response = requests.put(url, data=payload, headers=headers)

print "response is"
print response.text

