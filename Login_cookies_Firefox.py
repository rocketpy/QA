import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", "...")
driver = webdriver.Firefox(executable_path="...", options=options)

LOGIN = ""
PASSWORD = ""

try:
    # driver.get("https://instagram.com/")
    # time.sleep(5)
    #
    # username_input = driver.find_element_by_name("username")
    # username_input.clear()
    # username_input.send_keys(instagram_login)
    # time.sleep(5)
    #
    # password_input = driver.find_element_by_name("password")
    # password_input.clear()
    # password_input.send_keys(instagram_password)
    # time.sleep(5)
    #
    # password_input.send_keys(Keys.ENTER)
    # time.sleep(10)
    #
    # # # cookies
    # pickle.dump(driver.get_cookies(), open(f"{instagram_login}_cookies", "wb"))

    driver.get("https://instagram.com/")
    time.sleep(5)
