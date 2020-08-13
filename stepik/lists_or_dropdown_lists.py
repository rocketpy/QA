import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


LINK = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(LINK)
"""
browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("option:nth-child(2)").click()  
#  or
browser.find_element_by_css_selector("[value='1']").click()

# or by Select , it's a best practice !
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") 

# Select by visible text
select.select_by_visible_text("text")

#  Select by index
select.select_by_index(index)  # first index is 0
"""

try:
    first_num = browser.find_element_by_id("num1").text
    second_num = browser.find_element_by_id("num2").text
    result = int(first_num) + int(second_num)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(result))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
