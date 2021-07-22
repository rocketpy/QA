from appium import webdriver
from config import url


URL = 'https://www...'

DESIRE_CAPABILITY = {'platformName': 'iOS',
                     'platformVersion': '11.4',
                     'deviceName': 'iPhone X',
                     'browserName': 'Safari'
                    }

def test_open_website():
    driver = webdriver.Remote(URL, DESIRE_CAPABILITY)
    driver.get(url)
    current_url = driver.current_url
    assert url == current_url
    
