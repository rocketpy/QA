# for run a test with firefox browser:   pytest -s -v --browser_name=firefox test_file_name.py

from selenium import webdriver


driver = webdriver.Firefox()
driver.get("https://...")  # must opening a new window with FF


#  or
"""
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)

driver.get("https://...")
"""

#  or
"""
pip install webdriver_manager

from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
"""
