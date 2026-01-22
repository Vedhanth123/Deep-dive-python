# This file will contain explanation of the requests module in python

# requests module in python is used for POST, GET http requests
# it is basically a client side request sender but... in python. It is similar to fetch in javascript

# We will be first interacting with this url "https://xkcd.com/353"
import requests

req = requests.get('https://xkcd.com/353') # this is used for get requests

print(req) # gives out status code 200 if the request is successful.

# print(req.text) # this gives html (we can use html parser to parse this html code)

# print(req.content) # this is used to get the content (this returns the data in the form of bytes usually images)

''' ----------------------------------------------- Getting Image from web using python ---------------------------------------------------------------------------------
# I will try to fetch an image from web to python 
# 1) I need url of that image
reqImage = requests.get('https://rukminim2.flixcart.com/image/480/640/k5jxfgw0/sticker/d/m/f/joker-face-medium-53-dds412-divinedesigns-original-imafz7m5vrsjjs52.jpeg?q=90')
with open('joker.jpeg', 'wb') as f:
    
    f.write(reqImage.content)
'''

print(req.status_code) # prints the status code 

print(req.ok) # this prints true if there are no errors else false

print(req.headers)
