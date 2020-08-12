import time
from selenium import webdriver
from selenium.webdriver.common.by import By
 

LINK_1 = "http://suninjuly.github.io/registration1.html"
LINK_2 = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()

try:
    browser.get(LINK_1)
    # browser.get(LINK_2)

    input1 = browser.find_element_by_class_name("form-control.first")
    input1.send_keys("John")
    input2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
    input2.send_keys("Doe")
    input3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
    input3.send_keys("abc123@gmail.com")
    # input4 = browser.find_element_by_id("country")
    # input4.send_keys("")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(3)

    browser.quit()
