from selenium import webdriver


#PATH = "C:\Program Files\chromedriver.exe" 
#driver = webdriver.Chrome(PATH) 

PROXY = "12.345.678.910:8080"
options = WebDriverWait.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)
chrome = webdriver.Chrome(chrome_options=options)

TC_1 = ''
TC_2 = ''
TC_3 = ''
TC_4 = ''
TC_5 = ''
TC_6 = ''
TC_7 = ''
TC_8 = ''
TC_9 = ''
TC_10 = ''
TC_11 = ''
TC_12 = ''

driver.get("https://...")
