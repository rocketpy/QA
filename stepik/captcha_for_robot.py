import math
import time
from selenium import webdriver
# from selenium.webdriver.common.by import By
 
"""
LINK = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()

try:
    browser.get(LINK)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
      
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element_by_class_name("form-control")
    input_answer.send_keys(y)
    
    button_i_am_robot = browser.find_element_by_class_name("form-check-input")
    button_i_am_robot.click()
    
    button_robots_rule = browser.find_element_by_css_selector("[value='robots']")
    button_robots_rule.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)

    browser.quit()
"""

LINK = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()

try:
    browser.get(LINK)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element_by_xpath('//*[@id="treasure"]')
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    button_i_am_robot = browser.find_element_by_id("robotCheckbox")
    button_i_am_robot.click()

    button_robots_rule = browser.find_element_by_id("robotsRule")
    button_robots_rule.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)

    browser.quit()

