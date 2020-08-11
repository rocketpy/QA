from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()

browser.get("https://...")
submit_button = browser.find_element_by_id("submit")  # find a button by ID
# or
submit_button = browser.find_element(By.ID, "submit")  # using a universal method:  find_element()

