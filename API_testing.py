# pip install -U requests
# pip install -U pytest

import requests


def test_get_200():
     response = requests.get("http://api...")
     assert response.status_code == 200

      
