#  Apiritif - Python framework for API testing

# PyPi:  https://pypi.org/project/apiritif/
# Github: https://github.com/Blazemeter/apiritif


#  HTTP Requests
# Apiritif allows to use simple requests-like API for making HTTP requests.

from apiritif import http

response = http.get("http://...")
response.assert_ok()  # will raise AssertionError if request wasn't successful



