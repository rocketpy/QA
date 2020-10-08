from time import sleep
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType


#PATH = "C:\Program Files\chromedriver.exe" 
#driver = webdriver.Chrome(PATH) 

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
IP = PROXY[0, -5]

#  test cases for fields
TC_1 = ''  #  Empty value
TC_2 = '   12345abcABC'  #  Space values at the beginning
TC_3 = '1234567890'  # numerics
TC_4 = 'abcdefgh'  # lowercase alphabet
TC_5 = 'abcde   fgh'  #  Space in the middle
TC_6 = 'abcdefgh   '  #  Space values at the end
TC_7 = '<span class="text-gray">No suggested jump to results</span>'  #  Using HTML tag's
TC_8 = '!@#$%^&*()_+{}{}{}{:":"?><>PaSSword!@#$%^&*()-_+=`~/\,.?><|'  #  Special symbols
TC_9 = 'ABCDEFGH'  # uppercase alphabet
TC_10 = 'vasya_pupkin@@@gmail.com'  #  triple @@@
TC_11 = 'a'  # min alphabet value
TC_12 = '1'  # min numeric value
TC_13 = '               '  #  Space
TC_14 = 'भारतभारतभारतभारत网络网络网络网络'  #  Non ASCII
TC_15 = '<script>document.body.style.backgroundColor = "#000";</script>'
TC_16 = '$detail_id=$_GET['detail'];'
TC_17 = 'http://www.site.com/page.php?var=<script>alert('xss');</script>'  #  Basic XSS, Basic Sql injection, Average value
TC_18 = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx11111111111111111111111111111111111111111111111111
         xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx11111111111111111111111111111111111111111111111111
         xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx11111111111111111111111111111111111111111111111111
         xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx11111111111111111111111111111111111111111111111111
         xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx11111111111111111111111111111111111111111111111111
         xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx11111111111111111111111111111111111111111111111111'  # max value

cases_list = [TC_1, TC_2, TC_3, TC_4, TC_5, TC_6, TC_7, TC_8, TC_9, TC_10,
             TC_11, TC_12, TC_13, TC_14, TC_15, TC_16, TC_17, TC_18]         
         
# driver.get("https://...")


def auth_form_valid():
    try:
        driver.get("https://2ip.ru/")  # checking a proxy
        prox = driver.find_element_by_xpath("//*[@id="d_clip_button"]/span").text
         
        if prox == IP:
            driver.get("https://...")  
            time.sleep(2)
            name_field = driver.find_element_by_xpath('')  # input field 
            name_field.send_keys(NAME)
            time.sleep(1)
            surname_field = driver.find_element_by_xpath('')  # input field 
            surname_field.send_keys(SURNAME)
            time.sleep(1)
            email_field = driver.find_element_by_xpath('')  # input field 
            email_field.send_keys(EMAIL)
            time.sleep(1)
            password_field = driver.find_element_by_xpath('')  # input field 
            password_field.send_keys(PASSWORD)
            time.sleep(1)
            confirm_password_field = driver.find_element_by_xpath('')  # input field 
            confirm_password_field.send_keys(CONFIRM_PASSWORD)
            time.sleep(1)
            submit_button = driver.find_element_by_xpath('')  # submit button
            submit_button.click()
        else:
            driver.quit()
    except NoSuchElementException:
        print("Oooops , we have some problem !")

def auth_form():
    try:
        driver.get("https://2ip.ru/")  # checking a proxy
        prox = driver.find_element_by_xpath("//*[@id="d_clip_button"]/span").text
         
        if prox == IP:
            driver.get("https://...")
            time.sleep(2)
            for item in cases_list: 
                name_field = driver.find_element_by_xpath('')  # input field 
                name_field.send_keys(item)
            time.sleep(1)
            surname_field = driver.find_element_by_xpath('')  # input field 
            surname_field.send_keys("Abcdefgh")
            time.sleep(1)
            email_field = driver.find_element_by_xpath('')  # input field 
            email_field.send_keys("Abcdefgh")
            time.sleep(1)
            password_field = driver.find_element_by_xpath('')  # input field 
            password_field.send_keys("Abcdefgh")
            time.sleep(1)
            confirm_password_field = driver.find_element_by_xpath('')  # input field 
            confirm_password_field.send_keys("Abcdefgh")
            time.sleep(1)
            submit_button = driver.find_element_by_xpath('')  # submit button
            submit_button.click()   
        else:
            driver.quit()
        
    except NoSuchElementException:
        print("Oooops , we have some problem !")

#driver.quit()


if __name__ == '__main__':
    auth_form_valid()  # first checking a valid data
    auth_form()
    

