#!/usr/bin/python

import requests, json
import sys
import hashlib
import hmac
import binascii

try:
    if len(sys.argv[1]) > 0:
        username = sys.argv[1]
except IndexError:
    username = 'user'

try:
    if len(sys.argv[2]) > 0:
        ip = sys.argv[2]
except IndexError:
    ip = "172.16.78.135:8000"
    
url = "http://" + ip + "/poker/user/";
payload = json.dumps({'username':username}) 

testString = "foo"
key = "bar"
hashed = hmac.new(key, testString, digestmod=hashlib.sha256)
authHash = binascii.b2a_base64(hashed.digest()).strip()

authorization = "OAuth realm=\"mozilla\",oauth_signature_method=\"HMAC-SHA256\","
authorization += "oauth_key=\"" + key + "\","
authorization += "oauth_signature=\"" + authHash + "\","
authorization += "oauth_timestamp=\"now\""

headers = { "Content-type": "application/x-www-form-urlencoded", 
            "Accept": "text/plain",
            "Authorization": str(authorization)}

print "\nPosting to " + url + " with payload " + payload + "\n\n" + "with headers " + str(headers)
response = requests.put(url, data=payload, headers=headers)

print "\nresponse is\n"
print response.text

