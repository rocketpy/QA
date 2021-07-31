from appium import webdriver

 
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
wanted_caps ['deviceName'] = '1234567890123'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
 
driver = webdriver.Remote ('http: // localhost: 4723 / wd / hub', wanted_caps)
# driver.find_element_by_name("=").click() 
driver.quit () 
