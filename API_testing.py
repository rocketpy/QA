# pip install -U requests
# pip install -U pytest

# For run tests use:  pytest tests\my_project_tests.py

import requests


def test_get_200():
     response = requests.get("http://api...")
     assert response.status_code == 200

      
# Check if the value of the response content type header correctly
def test_check_header():
     response = requests.get("http://api...")
     assert response.headers["Content-Type"] == "application/json"
     
