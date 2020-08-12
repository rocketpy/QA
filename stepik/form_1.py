import time
from selenium import webdriver


browser = webdriver.Chrome()

try: 
    LINK = "http://suninjuly.github.io/registration2.html"
    # browser = webdriver.Chrome()
    browser.get(LINK)
    
    elements = browser.find_elements_by_tag_name("input")

    for element in elements:
        element.send_keys("Text")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(3)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
