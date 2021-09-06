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
     

# Checking the value of a response body element
def test_check_body_element():
    response = requests.get("http://api...")
    response_body = response.json()
    assert response_body["country"] == "Ukraine"


# Extract and assert on the value of the place name
def test_some_element():
    response = requests.get("http://api...")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == "Braiton"


# Checking len of values
def test_len_elems():
    response = requests.get("http://api...")
    response_body = response.json()
    assert len(response_body["places"]) == 1
  

# The test methods with arguments
@pytest.mark.parametrize("country_code, zip_code, expected_place_name", test_data_zip_codes)
def test_using_test_data_object_get_location_data_check_place_name(country_code, zip_code, expected_place_name):
    response = requests.get(f"http://api../{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place_name
    
