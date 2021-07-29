import unittest
# from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# Example for registration form


class Register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/chromedriver")
        self.driver.maximize_window()

def setUp(self):
    self.driver = webdriver.Firefox()
    self.driver.get("http://www...")
        
        
def test_main(self):
    driver.implicitly_wait(20)
    # driver = self.driver
    # driver.get("http://www...")
    driver.find_element_by_link_text("Registration").click()
    
    elem = driver.find_element_by_id("...")
    elem.send_keys("Some text")
    elem = driver.find_element_by_id("...")
    elem.send_keys("Some text")
    
    elem = driver.find_element_by_css_selector("...").click()
    elem = driver.find_element_by_xpath("...").click()
    
    # time.sleep(5)
    select = Select(driver.find_element_by_id('...'))
    select.select_by_visible_text('Some text')
    
    # date 
    select = Select(driver.find_element_by_id('...'))
    select.select_by_visible_text('...')
    
    # a day
    select = Select(driver.find_element_by_id('...'))
    select.select_by_visible_text('...')
    
    # a year
    select = Select(driver.find_element_by_id('...'))
    select.select_by_visible_text('...')
    
    # email and phone number
    elem = driver.find_element_by_id("...")
    elem.send_keys("...")
    elem = driver.find_element_by_id("...")
    elem.send_keys("...")
    
    # img of profile
    elem = driver.find_element_by_id("...")
    elem.send_keys("file name or path to file")
    
    # input passwords
    elem = driver.find_element_by_id("")
    elem.send_keys("...")
    elem = driver.find_element_by_id("...")
    elem.send_keys("...")
    # time.sleep(5)
    elem = driver.find_element_by_xpath("...").click()


    def tearDown(self):
         self.driver.close()


if __name__ == "__main__":
    unittest.test_main()
    
