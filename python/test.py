#!/usr/bin/env python3
# -*- coding: UTF-8 -*-# enable debugging
import cgitb
import requests

cgitb.enable()
r = requests.get('https://tfngbfhvqd.execute-api.us-east-1.amazonaws.com/deploymenttest/kakuro?toplength=3&topsum=7&sidelength=3&sidesum=10')

print("Content-Type: Content-type: text/html\n")
print(str(r.text))
#print ("hello world")
