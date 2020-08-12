import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# driver.find_elements(By.CSS_SELECTOR, "button.submit")  # for searching elements , or use find_elements_by_ ()

#  VERY Important , if find_element() NOT find elem , reise NoSuchElementException  !!!
#  But if find_elements() NOTHING find , he will return empty list 


browser.get("https://fake-shop.com/book1.html")

# adding unit (goods) to cart
add_button = browser.find_element_by_css_selector(".add")
add_button.click()

# open second unit page
browser.get("https://fake-shop.com/book2.html")

# adding unit to cart
add_button = browser.find_element_by_css_selector(".add")
add_button.click()

# opening a cart
browser.get("https://fake-shop.com/basket.html")

# searching a list of all units (goods)
goods = browser.find_elements_by_css_selector(".good")

# checking for a ammount of units = 2
assert len(goods) == 2

browser.quit()
