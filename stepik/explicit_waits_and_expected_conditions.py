import math
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
      
    price = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@id="price"]"),"$100"))
    
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()

    x_element = browser.find_element_by_xpath('//*[@id="treasure"]')
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)

    browser.quit()


button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
button.click()

