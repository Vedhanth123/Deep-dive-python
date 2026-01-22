# This file is uses "https://httpsbin.org" to test our requests module. Actually this website
# was written by the creator of the requests module to test the requests module



import requests

# to demo get request
'''
# adding parameters to the url might be prone to errors
# so requests library allows us to send out query parameters in the form of dictionary
payload = {'page':2, 'count': 25}
req = requests.get('https://httpbin.org/get', params=payload) # this is same as https://httpbin.org/get?page=2&count=25

print(req.text) # we get response
'''


# to demonstrate post request
'''
payload = {'username':'vedhanth',
           'password':'test'}
req = requests.post("https://httpbin.org/post", data=payload)

# print(req.text)

# we usually get json responses from the http requests
# Another thing to remember is that json() function is requests is possible because Json module is 
# already imported in the requests module
reqDict = req.json() # this creates a python dictionary from the json response

print(reqDict['form'])
'''

# demo basic authentication
'''
req = requests.get('https://httpbin.org/basic-auth/vedhanth/tst', auth=("vedhanth",'test'), timeout=2) # auth contains a tuple of username and password

print(req.status_code)
print(req.text)
'''

# demo timeout
req = requests.get("https://httpbin.org/delay/5", timeout=2) # this link usually gives response in 5 seconds but we are forcing our 
# reqest function stop after 2 seconds soo this will raise an exception stating its timeed out.


