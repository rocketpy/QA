import os 
import math
import time
from selenium import webdriver


current_dir = os.path.abspath(os.path.dirname(__file__))    # get cwd (current directory)
file_path = os.path.join(current_dir, 'file.txt')           # adding to this path a file name
element.send_keys(file_path)

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

