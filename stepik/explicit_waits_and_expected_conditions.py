import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


LINK = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()

try:
    browser.get(LINK)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
      
    price = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='price']"), "$100"))
    
    button_book = browser.find_element_by_css_selector("button.btn.btn-primary")
    button_book.click()

    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x_element.text
    y = calc(int(x))

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    button = browser.find_element_by_xpath("//*[@id='solve']")
    button.click()

finally:
    time.sleep(7)
    browser.quit()


# button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
# button.click()

#  FOR case , when page too long downloading :
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


link = ""
caps = DesiredCapabilities.CHROME
browser = webdriver.Chrome(desired_capabilities=caps)
caps["pageLoadStrategy"] = "none"
browser.get(link)

# waiting when elem be downloaded
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".example_selector"))) 

# make a stop for downloading a page
browser.execute_script("window.stop();")
"""

