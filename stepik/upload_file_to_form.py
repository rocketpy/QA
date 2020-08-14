import os 
import math
import time
from selenium import webdriver


current_dir = os.path.abspath(os.path.dirname(__file__))    # get cwd (current directory)
file_path = os.path.join(current_dir, 'file.txt')           # adding to this path a file name
# element.send_keys(file_path)

LINK = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()

try:
    browser.get(LINK)

    first_name = browser.find_element_by_xpath("/html/body/div/form/div/input[1]")
    first_name.send_keys("John")
    
    last_name = browser.find_element_by_xpath("/html/body/div/form/div/input[2]")
    last_name.send_keys("Doe")
    
    email = browser.find_element_by_xpath("/html/body/div/form/div/input[3]")
    email.send_keys("abc123@gmail.com")
    
    upload_file = browser.find_element_by_id("file")
    upload_file.send_keys("file_path")

    submit_button = browser.find_element_by_css_selector("button.btn")
    submit_button.click()

finally:
    time.sleep(5)

    browser.quit()
