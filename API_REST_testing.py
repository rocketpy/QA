#  install requirements
#  pip install -U requests Flask pytest pytest-html


import json
import requests

# for run this test with pytest use: pytest  

def test_post_headers_body_to_json():
    url = 'https://httpbin.org/post'
    headers = {'Content-Type': 'application/json'} 
    payload = {'key1': 1, 'key2': 'value2'}
    # need convert dict to json string by json.dumps() for body data. 
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))    
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['url'] == url
    # print(resp.text)
    
    
#  some example from Postman (create a Postman API request test and take code )
"""
import requests


url = "http://httpbin.org/post"
payload = "{...}"
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
