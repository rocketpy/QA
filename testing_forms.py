from selenium import webdriver


#PATH = "C:\Program Files\chromedriver.exe" 
#driver = webdriver.Chrome(PATH) 

PROXY = "12.345.678.910:8080"
options = WebDriverWait.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)
chrome = webdriver.Chrome(chrome_options=options)

#  test cases
TC_1 = ''
TC_2 = '   12345abcABC'
TC_3 = '1234567890'
TC_4 = 'abcdefgh'
TC_5 = 'abcde   fgh'
TC_6 = 'abcdefgh   '
TC_7 = '<span class="text-gray">No suggested jump to results</span>'
TC_8 = '!@#$%^&*()_+{}{}{}{:":"?><>'
TC_9 = 'ABCDEFGH'
TC_10 = 'vasya_pupkin@@@gmail.com'
TC_11 = 'a'
TC_12 = '1'
TC_13 = '<script>document.body.style.backgroundColor = "#000";</script>'
TC_14 = '$detail_id=$_GET['detail'];'
TC_15 = 'http://www.site.com/page.php?var=<script>alert('xss');</script>'

driver.get("https://...")
