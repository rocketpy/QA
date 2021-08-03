import unittest
# from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# Example for registration form

# Important !!!  Here needed to add asserts !!!


class Register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/chromedriver")
        self.driver.maximize_window()

def setUp(self):
    self.driver = webdriver.Firefox()
    self.driver.get("http://www...")
        
        
def test_main(self):
    driver.implicitly_wait(20)
    buttn_reg = driver.find_element_by_link_text("Registration")
    buttn_reg.click()
    self.assertTrue(buttn_reg), "No such button found."
    
    elem = driver.find_element_by_id("...")
    elem.send_keys("Some text")
    self.assertTrue(elem), "No such element found."
    
    elem_2 = driver.find_element_by_id("...")
    elem_2.send_keys("Some text")
    self.assertTrue(elem_2), "No such element found."
    
    elem = driver.find_element_by_css_selector("...").click()
    elem_2 = driver.find_element_by_xpath("...").click()
    
    # time.sleep(5)
    select = Select(driver.find_element_by_id('...'))
    select.select_by_visible_text('Some text')
    self.assertTrue(select), "No such element found."
    
    # date 
    select = Select(driver.find_element_by_id('...'))
    select.select_by_visible_text('...')
    # self.assertTrue(), "No such element found."
    
    # a day
    select = Select(driver.find_element_by_id('...'))
    select.select_by_visible_text('...')
    # self.assertTrue(), "No such element found."
    
    # a year
    select = Select(driver.find_element_by_id('...'))
    select.select_by_visible_text('...')
    # self.assertTrue(), "No such element found."
    
    # email and phone number
    elem = driver.find_element_by_id("...")
    elem.send_keys("...")
    # self.assertTrue(), "No such element found."
    
    elem = driver.find_element_by_id("...")
    elem.send_keys("...")
    # self.assertTrue(), "No such element found."
    
    # img of profile
    elem = driver.find_element_by_id("...")
    elem.send_keys("file name or path to file")
    # self.assertTrue(), "No such element found."
    
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
    unittest.main()
    
