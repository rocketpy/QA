import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", "...")
driver = webdriver.Firefox(executable_path="...", options=options)

LOGIN = ""
PASSWORD = ""

#  IMPORTANT , first step , make auth with real phone numb and password
try:
    driver.get("https://www...")
    time.sleep(5)
    
    username_input = driver.find_element_by_name("LOGIN")
    username_input.clear()
    username_input.send_keys(instagram_login)
    time.sleep(5)
    
    password_input = driver.find_element_by_name("PASSWORD")
    password_input.clear()
    password_input.send_keys(instagram_password)
    time.sleep(5)
    
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)
    
    # get a cookies
    pickle.dump(driver.get_cookies(), open(f"{LOGIN}_cookies", "wb"))

    #  This part for Login with cookies,  using this part for auth with cookies !!!
    # driver.get("https://www...")
    #vtime.sleep(5)
    
    # for cookie in pickle.load(open(f"{LOGIN}_cookies", "rb")):
    #    driver.add_cookie(cookie)

    # time.sleep(5)
    # driver.refresh()  # update a page
    # time.sleep(5)

except Exception as ex:
    print(ex)
    
finally:
    driver.close()
    driver.quit()
    
    
