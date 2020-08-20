from selenium.webdriver.chrome.options import Options
#  Options using for: set language, set proxy , different versions of browsers !!!  

#  set language for Chrome
options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

# set language for Firefox
fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)
