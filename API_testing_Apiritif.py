#  Apiritif - Python framework for API testing

# PyPi:  https://pypi.org/project/apiritif/
# Github: https://github.com/Blazemeter/apiritif


#  HTTP Requests
# Apiritif allows to use simple requests-like API for making HTTP requests.

from apiritif import http

response = http.get("http://...")
response.assert_ok()  # will raise AssertionError if request wasn't successful


#  http object provides the following methods:

from apiritif import http

http.get("http://api.example.com/posts")
http.post("http://api.example.com/posts")
http.put("http://api.example.com/posts/1")
http.patch("http://api.example.com/posts/1")
http.delete("http://api.example.com/posts/1")
http.head("http://api.example.com/posts")
# All methods (get, post, put, patch, delete, head) support the following arguments:

def get(address,               # URL for the request
        params=None,           # URL params dict
        headers=None,          # HTTP headers
        cookies=None,          # request cookies
        data=None,             # raw request data
        json=None,             # attach JSON object as request body
        encrypted_cert=None,   # certificate to use with request 
        allow_redirects=True,  # automatically follow HTTP redirects
        timeout=30)            # request timeout, by default it's 30 seconds


#  for more info go to Docs

