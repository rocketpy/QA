"""
#  docs:  https://docs.python.org/3/library/unittest.html
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()
"""
    
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
 

LINK_1 = "http://suninjuly.github.io/registration1.html"
LINK_2 = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()

try:
    browser.get(LINK_1)
    # browser.get(LINK_2)

    input1 = browser.find_element_by_class_name("form-control.first")
    input1.send_keys("John")
    input2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
    input2.send_keys("Doe")
    input3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
    input3.send_keys("abc123@gmail.com")
    # input4 = browser.find_element_by_id("country")
    # input4.send_keys("")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(3)
    browser.quit()


class TestForms(unittest.TestCase):
    def test_form_1(self):
        browser.get(LINK_1)

        input1 = browser.find_element_by_class_name("form-control.first")
        input1.send_keys("John")
        input2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
        input2.send_keys("Doe")
        input3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("abc123@gmail.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        
        time.sleep(3)
        browser.quit()
        
        self.assertEqual(, , "Should be ...")
        
    def test_form_2(self):
        browser.get(LINK_2)
        input1 = browser.find_element_by_class_name("form-control.first")
        input1.send_keys("John")
        input2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
        input2.send_keys("Doe")
        input3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("abc123@gmail.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        
        time.sleep(3)
        browser.quit()
        
        self.assertEqual(, , "Should be ...")
        
        
if __name__ == "__main__":
    unittest.main()
    
