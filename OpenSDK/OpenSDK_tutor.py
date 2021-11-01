#  OpenSDK - Test Automation platform for Web, Mobile and API testing.

# PyPI: https://pypi.org/project/testproject-python-sdk/
# Docs: https://testproject.io/
# Github: https://github.com/testproject-io/python-opensdk

# Minimum Python version required is 3.6

# pip install testproject-python-sdk
# or
# pip3 install testproject-python-sdk


# Test Development
"""
Using a TestProject driver is identical to using a Selenium driver.
Once you have added the SDK as a dependency to your project, changing the import statement is enough in most cases.
You can create a TestProject-powered version of a test using Chrome by using the TestProject Chrome driver:
"""

# from selenium import webdriver  <-- replace this import
from src.testproject.sdk.drivers import webdriver


def test_create_a_chrome_driver_instance():
    driver = webdriver.Chrome()
    
    # Your test code goes here
    driver.quit()


