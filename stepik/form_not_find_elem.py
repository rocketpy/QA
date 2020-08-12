import time
from selenium import webdriver
 

LINK_1 = "http://suninjuly.github.io/registration1.html"
LINK_2 = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()

try:
    # browser = webdriver.Chrome()
    browser.get(LINK_1)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("John")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Doe")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("abc123@gmail.com")
    # input4 = browser.find_element_by_id("country")
    # input4.send_keys("")
    button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    time.sleep(30)

    browser.quit()
