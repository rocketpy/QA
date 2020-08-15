import time
from selenium import webdriver


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

time.sleep(2)  # waiting 2 seconds for download a button
button = browser.find_element_by_id("verify")
button.click()

message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
