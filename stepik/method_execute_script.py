import time
from selenium import webdriver


LINK = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(LINK)
"""
# make a simple example with alert on web page
browser.execute_script("alert('Robots at work');")
#  or
browser.execute_script("document.title='Script executing';")

# two and more commands in one
browser.execute_script("document.title='Script executing';alert('Robots at work');")  # change title and call alert
"""

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
      
    x = browser.find_element_by_id('input_value').text
    y = calc(int(x))
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
    time.sleep(1)
    
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
