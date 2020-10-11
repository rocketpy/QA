#  http://jsonplaceholder.typicode.com  - Fake online for testing REST API (JSON Server )
import requests


#  API calls 
url = 'http://jsonplaceholder.typicode.com/photos'
response = requests.get(url)  # API call
# print(response.json())
json_payload = {'albumID': 1, 'title': 'test', 'url': 'test.com'}
resp_post = requests.post(url, json=json_payload)
resp_post.json()

url_2 = 'http://jsonplaceholder.typicode.com/photos/100'
resp_post = requests.put(url, json=json_payload)
resp_post.json()

resp_post = requests.delete(url, json=json_payload)
resp_post.json()

#  API authentication
import requests


url = 'https://api.github.com/user'
response = requests.get(url)
response.json()

response = requests.get(url, auth=('test_name', 'password'))
response.json()

#  with user Token 
response = requests.get(url, headers={'Autorization': 'Bearer here put user token'})
response.json()

#  get all keys in json
resp = response.json()
for key in resp.keys():
    print(key)
    
    
#  task , find duplicates of photo uls
import requests

url = 'http://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
json_data = response.json()
list_urls = []
for photo in json_data:
    list_urls.append(photo[url])

uniq_urls = set(list_urls)  # here contain only uniq urls

