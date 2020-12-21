#  install requirements
#  pip install -U requests Flask pytest pytest-html



#  some example from Postman (create a Postman API request test and take code )
"""
import requests


url = "http://httpbin.org/post"
payload = "{\n    \"key1\": 1,\n    \"key2\": \"value2\"\n}"
headers = {
    'Content-Type': "",
    'User-Agent': "Postman",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "",
    'Host': "httpbin.org",
    'accept-encoding': "",
    'content-length': "",
    'Connection': "",
    'cache-control': ""
    }

response = requests.request("POST", url, data=payload, headers=headers)
# print(response.text)
"""
