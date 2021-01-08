import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import vk_password, vk_phone


options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

driver = webdriver.Chrome(executable_path="/home/cain/PycharmProjects/selenium_python/chromedriver/chromedriver",
                          options=options
                         )


try:
    # driver.get("https://...")
    # time.sleep(5)
    #
    # email_input = driver.find_element_by_id("index_email")
    # email_input.clear()
    # email_input.send_keys(vk_phone)
    # time.sleep(5)
    #
    # password_input = driver.find_element_by_id("index_pass")
    # password_input.clear()
    # password_input.send_keys(vk_password)
    # time.sleep(3)
    # password_input.send_keys(Keys.ENTER)
    #
    # # login_button = driver.find_element_by_id("index_login_button").click()
    # time.sleep(10)
    #
    # news_link = driver.find_element_by_id("l_nwsf").click()
    # time.sleep(5)
    #
    # # cookies
    # pickle.dump(driver.get_cookies(), open(f"{vk_phone}_cookies", "wb"))

    driver.get("https://.../")
    time.sleep(3)

    for cookie in pickle.load(open(f"{vk_phone}_cookies", "rb")):
        driver.add_cookie(cookie)

    time.sleep(3)
    driver.refresh()
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
