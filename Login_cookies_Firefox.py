import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", "...")
driver = webdriver.Firefox(executable_path="...", options=options)

LOGIN = ""
PASSWORD = ""
