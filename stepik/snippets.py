from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = "https://..."
browser = webdriver.Chrome()

browser.get("https://...")  # or  browser.get(LINK)
submit_button = browser.find_element_by_id("submit")  # find a button by ID
submit_button.click()
# or
submit_button = browser.find_element(By.ID, "submit")  # using a universal method:  find_element()
submit_button.click()

# find_element() ,  RETURN Only FIRST element !!!  For others elems need use find_elements_by...()  !!!

# By.ID , By.CSS_SELECTOR , By.XPATH , By.NAME , By.TAG_NAME , By.CLASS_NAME , By.LINK_TEXT , By.PARTIAL_LINK_TEXT 

#  browser.close() , closing only current window , not all opened pages !!!
browser.quit()


# using Try/Finally
try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    submit_button = browser.find_element(By.ID, "submit_button")
    button.click()
finally:  # will quit in anyway
    browser.quit()

#  or , best way
with webdriver.Chrome() as browser:
    browser.get(LINK)
    submit_button = browser.find_element(By.ID, "submit")
    button.click()
