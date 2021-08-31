from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType


#PATH = "C:\Program Files\chromedriver.exe" 
#driver = webdriver.Chrome(PATH) 

"""
options = webdriver.ChromeOptions()
options.add_argument("user-agent=...")

#  webdriver mode OFF

#  for ChromeDriver under version 79.0.3945.16
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

# for ChromeDriver version 79.0.3945.16 or higher
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(executable_path="...",
                          options=options
                         )
                         
driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")  # checking , working or not a mode_off !
"""

options = Options()
# options.add_argument('--headless')
options.add_argument("start-maximized")
options.add_argument('disable-infobars')  # disable infobar in Chrome browser
# driver = webdriver.Chrome(chrome_options=options, executable_path=r'/Users/.../chromedriver')

#  for Chrome
opts = Options()
user_agent = "any agent"
opts.add_argument("user-agent=user_agent")
driver = webdriver.Chrome(chrome_options=opts)

"""
prox = Proxy()
prox.proxy_type = ProxyType.MANUAL

prox.http_proxy = “0.0.0.0:00000”
prox.socks_proxy = “0.0.0.0:00000”
prox.ssl_proxy = “0.0.0.0:00000”

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

# configure ChromeOptions
driver = webdriver.Chrome(executable_path='/usr/local/share chromedriver',desired_capabilities=capabilities)

# verify proxy ip
driver.get("http://www.whatsmyip.org/")
"""

PROXY = "12.345.678.910:8080"  #  for HTTP
PROXY_S = "12.345.678.910:443"  #  for HTTPS
options = WebDriverWait.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)
chrome = webdriver.Chrome(chrome_options=options)

#  CONSTS for validation
NAME = "Vasya"
SURNAME = "Pupkin"
EMAIL = "vasya_pupkin@gmail.com"  # it's a fake email
LOGIN = "v_pupkin"
PASSWORD = "12345qwerty"
CONFIRM_PASSWORD = PASSWORD

#  need change slice for each proxy !!!!!
IP = PROXY[0, -5]
#  IP = PROXY_S[0, -5]

#  test cases for fields
TC_1 = ''  #  Empty value
TC_2 = '   abcde'  #  Space values at the beginning
TC_3 = '1234567890'  # numerics
TC_4 = 'abcdefgh'  # lowercase alphabet
TC_5 = 'abcde   fgh'  #  Space in the middle
TC_6 = 'abcdefgh   '  #  Space values at the end
TC_7 = '<span class="text-gray">No suggested jump to results</span>'  #  Using HTML tag's
TC_8 = '«♣☺♂«»‘~!@#$%^&*()?>,./\<][ /*!@#$%^&*()_+{}{}{}{:":"?><>PaSSword!@#$%^&*()-_+=`~/\,.?><|'  #  Special symbols
TC_9 = 'ABCDEFGH'  # uppercase alphabet
TC_10 = 'vasya_pupkin@@@gmail.com'  #  triple @@@
TC_11 = 'a'  # min alphabet value
TC_12 = '1'  # min numeric value
TC_13 = '               '  #  Space
TC_14 = 'भारतभारतभारतभारत网络网络网络网络'  #  Non ASCII
TC_15 = '<script>document.body.style.backgroundColor = "#000";</script>'
TC_16 = '$detail_id=$_GET["detail"];'
TC_17 = 'http://www.site.com/page.php?var=<script>alert("xss");</script>'  #  Basic XSS, Basic Sql injection, Average value
TC_18 = '<script>alert(123)</script>'
TC_19 = 'DROP TABLE users;'  # for username or login fields !
TC_20 = 'SELECT * FROM blog WHERE code LIKE ‘a%’;'
TC_21 = '<script>alert(«Hello, world!»)</script>'
TC_22 = '<script>document.getElementByID(«…»).disabled=true</script>'
TC_23 = 'abcdeABCDE'  # upper and lower cases
TC_24 = '%%%%%%'
TC_25 = '<'+f'{LOGIN}'+'>'  # need use valid user with angle brackets
TC_26 = 'логинпароль'  # kirilica alphabet
TC_27 = ''  # checking ban for IP, for example 5 times possible to try login with wrong a password 
TC_28 = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx11111111111111111111111111111111111111111111111111
         xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx11111111111111111111111111111111111111111111111111
         xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx11111111111111111111111111111111111111111111111111
         xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx11111111111111111111111111111111111111111111111111
         xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx11111111111111111111111111111111111111111111111111
         xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx11111111111111111111111111111111111111111111111111'  # max value

cases_list = [TC_1, TC_2, TC_3, TC_4, TC_5, TC_6, TC_7, TC_8, TC_9, TC_10,
             TC_11, TC_12, TC_13, TC_14, TC_15, TC_16, TC_17, TC_18, TC_19,
             TC_20, TC_21, TC_22, TC_23, TC_24, TC_25, TC_26, TC_27]         

# got to previous url use:  driver.back()
# go to next url use:  driver.forward() 

def auth_form_valid():
    try:
        driver.get("https://2ip.ru/")  # checking a proxy
        driver.implicitly_wait(20) 
        prox = driver.find_element_by_xpath("//*[@id="d_clip_button"]/span").text
        # time.sleep(5)
        if prox == IP:
            driver.get("https://...")  # website wich contain web_form
            # time.sleep(5)
            name_field = driver.find_element_by_xpath('')  # input field 
            name_field.send_keys(NAME)
            # time.sleep(1)
            surname_field = driver.find_element_by_xpath('')  # input field 
            surname_field.send_keys(SURNAME)
            # time.sleep(1)
            email_field = driver.find_element_by_xpath('')  # input field 
            email_field.send_keys(EMAIL)
            # time.sleep(1)
            password_field = driver.find_element_by_xpath('')  # input field 
            password_field.send_keys(PASSWORD)
            # time.sleep(1)
            confirm_password_field = driver.find_element_by_xpath('')  # input field 
            confirm_password_field.send_keys(CONFIRM_PASSWORD)
            # time.sleep(1)
            submit_button = driver.find_element_by_xpath('')  # submit button
            submit_button.click()
            # time.sleep(2)
        else:
            driver.quit()
    except NoSuchElementException:
        print("Oooops , we have some problem !")

def auth_form_name():
    try:
        driver.get("https://2ip.ru/")  # checking a proxy
        driver.implicitly_wait(20) 
        prox = driver.find_element_by_xpath("//*[@id="d_clip_button"]/span").text
        # time.sleep(5)
        if prox == IP:
            driver.get("https://...")
            # time.sleep(5)
            for item in cases_list: 
                name_field = driver.find_element_by_xpath('')  # input field 
                name_field.send_keys(item)
                # tiem.sleep(1)
                surname_field = driver.find_element_by_xpath('')  # input field 
                surname_field.send_keys(SURNAME)
                # time.sleep(1)  
                email_field = driver.find_element_by_xpath('')  # input field 
                email_field.send_keys(EMAIL)  
                # time.sleep(1)  
                password_field = driver.find_element_by_xpath('')  # input field 
                password_field.send_keys(PASSWORD)
                # time.sleep(1)
                password_field = driver.find_element_by_xpath('')  # input field 
                password_field.send_keys(CONFIRM_PASSWORD)         
                # time.sleep(1)  
                submit_button = driver.find_element_by_xpath('')  # submit button
                submit_button.click() 
                # time.sleep(5)   
        else:
            driver.quit()
        
    except NoSuchElementException:
        print("Oooops , we have some problem !")

def auth_form_surname():
    try:
        driver.get("https://2ip.ru/")  # checking a proxy
        driver.implicitly_wait(20) 
        prox = driver.find_element_by_xpath("//*[@id="d_clip_button"]/span").text
        # time.sleep(5)
        if prox == IP:
            driver.get("https://...")
            # time.sleep(5)
            for item in cases_list: 
                name_field = driver.find_element_by_xpath('')  # input field 
                name_field.send_keys(NAME)
                # tiem.sleep(1)
                surname_field = driver.find_element_by_xpath('')  # input field 
                surname_field.send_keys(item)
                # time.sleep(1)  
                email_field = driver.find_element_by_xpath('')  # input field 
                email_field.send_keys(EMAIL)  
                # time.sleep(1)  
                password_field = driver.find_element_by_xpath('')  # input field 
                password_field.send_keys(PASSWORD)
                # time.sleep(1)
                password_field = driver.find_element_by_xpath('')  # input field 
                password_field.send_keys(CONFIRM_PASSWORD)         
                # time.sleep(1)  
                submit_button = driver.find_element_by_xpath('')  # submit button
                submit_button.click() 
                # time.sleep(5)  
        else:
            driver.quit()      
                  
    except NoSuchElementException:
        print("Oooops , we have some problem !")

def auth_form_email():
    try:
        driver.get("https://2ip.ru/")  # checking a proxy
        driver.implicitly_wait(20) 
        prox = driver.find_element_by_xpath("//*[@id="d_clip_button"]/span").text
        if prox == IP:
            driver.get("https://...")
            # time.sleep(2)
            for item in cases_list: 
                name_field = driver.find_element_by_xpath('')  # input field 
                name_field.send_keys(NAME)
                # tiem.sleep(5)
                surname_field = driver.find_element_by_xpath('')  # input field 
                surname_field.send_keys(SURNAME)
                # time.sleep(1)  
                email_field = driver.find_element_by_xpath('')  # input field 
                email_field.send_keys(item)  
                # time.sleep(1)  
                password_field = driver.find_element_by_xpath('')  # input field 
                password_field.send_keys(PASSWORD)
                # time.sleep(1)
                password_field = driver.find_element_by_xpath('')  # input field 
                password_field.send_keys(CONFIRM_PASSWORD)         
                # time.sleep(1)  
                submit_button = driver.find_element_by_xpath('')  # submit button
                submit_button.click()
                # time.sleep(5)
        else:
            driver.quit()
         
    except NoSuchElementException:
        print("Oooops , we have some problem !")

def auth_form_password():
    try:
        driver.get("https://2ip.ru/")  # checking a proxy
        driver.implicitly_wait(20) 
        prox = driver.find_element_by_xpath("//*[@id="d_clip_button"]/span").text
        if prox == IP:
            driver.get("https://...")
            time.sleep(5)
            for item in cases_list: 
                name_field = driver.find_element_by_xpath('')  # input field 
                name_field.send_keys(NAME)
                # tiem.sleep(1)
                surname_field = driver.find_element_by_xpath('')  # input field 
                surname_field.send_keys(SURNAME)
                # time.sleep(1)  
                email_field = driver.find_element_by_xpath('')  # input field 
                email_field.send_keys(EMAIL)  
                # time.sleep(1)  
                password_field = driver.find_element_by_xpath('')  # input field 
                password_field.send_keys(item)
                # time.sleep(1) 
                password_field = driver.find_element_by_xpath('')  # input field 
                password_field.send_keys(CONFIRM_PASSWORD)
                # time.sleep(1)           
                submit_button = driver.find_element_by_xpath('')  # submit button
                submit_button.click()
                # time.sleep(5)
        else:
            driver.quit()
         
    except NoSuchElementException:
        print("Oooops , we have some problem !")

def auth_form_confirm_password():
    try:
        driver.get("https://2ip.ru/")  # checking a proxy
        driver.implicitly_wait(20) 
        prox = driver.find_element_by_xpath("//*[@id="d_clip_button"]/span").text
        if prox == IP:
            driver.get("https://...")
            # time.sleep(5)
            for item in cases_list: 
                name_field = driver.find_element_by_xpath('')  # input field 
                name_field.send_keys(NAME)
                # time.sleep(1)
                surname_field = driver.find_element_by_xpath('')  # input field 
                surname_field.send_keys(SURNAME)
                # time.sleep(1)  
                email_field = driver.find_element_by_xpath('')  # input field 
                email_field.send_keys(EMAIL)  
                # time.sleep(1)  
                password_field = driver.find_element_by_xpath('')  # input field 
                password_field.send_keys(PASSWORD)
                # time.sleep(1)  
                password_field = driver.find_element_by_xpath('')  # input field 
                password_field.send_keys(item)
                # time.sleep(1)                   
                submit_button = driver.find_element_by_xpath('')  # submit button
                submit_button.click()
                # time.sleep(5)
        else:
            driver.quit()
         
    except NoSuchElementException:
        print("Oooops, we have some problem !")

#  driver.back()
#  driver.quit()

if __name__ == '__main__':
    auth_form_valid()  # first checking with a valid data
    auth_form_name()
    auth_form_surname()
    auth_form_email()
    auth_form_password()
    auth_form_confirm_password()
