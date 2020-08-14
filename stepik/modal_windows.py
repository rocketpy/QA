import math
import time
from selenium import webdriver

 
"""
# call modal window by JS
alert('Hello!');

# press button 'Ok' on modal window , named ALERT
alert = browser.switch_to.alert
alert.accept()

# Get a Text from modal window:
alert = browser.switch_to.alert
alert_text = alert.text

# Modal window with 'Ok' and 'Cancel' , named CONFIRM
confirm = browser.switch_to.alert
confirm.accept()  # press Ok
# and
confirm.dismiss()  # press 'Cancel'

# Modal window with input field, named PROMPT
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
"""

LINK = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(LINK)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    first_button = browser.find_element_by_css_selector("button.btn")
    first_button.click()
    
    alert_window = browser.switch_to.alert
    alert_window.accept()
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(int(x))
    
    input_answer = browser.find_element_by_class_name("form-control")
    input_answer.send_keys(str(y))
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(7)
    browser.quit()
