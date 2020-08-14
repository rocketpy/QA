import math
import time
from selenium import webdriver


"""
#  get a current page name (number)
current_window = browser.current_window_handle

# go to window_name:
browser.switch_to.window(window_name)

# name a second opened window
new_window = browser.window_handles[1]

# first window name
first_window = browser.window_handles[0]
"""

LINK = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(LINK)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    first_button = browser.find_element_by_css_selector("button.trollface.btn")
    first_button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    # alert_window = browser.switch_to.alert
    # alert_window.accept()
    
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
