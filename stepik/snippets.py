from selenium import webdriver


browser = webdriver.Chrome()

browser.get("https://...")
submit_button = browser.find_element_by_id("submit")  # find a button by ID
