#  http://jsonplaceholder.typicode.com  - Fake online for testing REST API (JSON Server )
import requests


url = 'http://jsonplaceholder.typicode.com/photos'
response = requests.get(url)  # API call
# print(response.json())
json_payload = {'albumID': 1, 'title': 'test', 'url': 'test.com'}
resp_post = requests.post(url, json=json_payload)
resp_post.json()


url_2 = 'http://jsonplaceholder.typicode.com/photos/100'
resp_post = requests.put(url, json=json_payload)
resp_post.json()
