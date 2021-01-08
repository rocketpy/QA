import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


PHONE_NUMB = ""
PASSWORD = ""


options = webdriver.ChromeOptions()
options.add_argument("user-agent=...")
driver = webdriver.Chrome(executable_path="...", options=options)

#  IMPORTANT , first step , make auth with real phone numb and password
try:
    driver.get("https://...")
    time.sleep(5)
    
    email_input = driver.find_element_by_id("index_email")
    email_input.clear()
    email_input.send_keys(PHONE_NUMB)
    time.sleep(5)
    
    password_input = driver.find_element_by_id("index_pass")
    password_input.clear()
    password_input.send_keys(PASSWORD)
    time.sleep(3)
    password_input.send_keys(Keys.ENTER)
    
    login_button = driver.find_element_by_id("index_login_button").click()
    time.sleep(5)
    
    news_link = driver.find_element_by_id("l_nwsf").click()
    time.sleep(5)
    
    # creating a file with cookies !!!
    pickle.dump(driver.get_cookies(), open(f"{PHONE_NUMB}_cookies", "wb"))

    # driver.get("https://.../")
    # time.sleep(3)

    # for cookie in pickle.load(open(f"{PHONE_NUMB}_cookies", "rb")):
    #    driver.add_cookie(cookie)

    time.sleep(3)
    driver.refresh()  # using for update a page
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

    
#  second step , using this part for auth with cookies !!!

try:
    """
    driver.get("https://...")
    time.sleep(5)
    
    email_input = driver.find_element_by_id("index_email")
    email_input.clear()
    email_input.send_keys(PHONE_NUMB)
    time.sleep(5)
    
    password_input = driver.find_element_by_id("index_pass")
    password_input.clear()
    password_input.send_keys(PASSWORD)
    time.sleep(3)
    password_input.send_keys(Keys.ENTER)
    
    login_button = driver.find_element_by_id("index_login_button").click()
    time.sleep(5)
    
    news_link = driver.find_element_by_id("l_nwsf").click()
    time.sleep(5)
    
    # creating a file with cookies !!!
    pickle.dump(driver.get_cookies(), open(f"{PHONE_NUMB}_cookies", "wb"))
    """
    driver.get("https://.../")
    time.sleep(3)

    for cookie in pickle.load(open(f"{PHONE_NUMB}_cookies", "rb")):
        driver.add_cookie(cookie)

    time.sleep(3)
    driver.refresh()
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

    
