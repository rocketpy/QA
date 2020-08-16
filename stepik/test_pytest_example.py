import time
import unittest
from selenium import webdriver


LINK_1 = "http://suninjuly.github.io/registration1.html"
LINK_2 = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()


class TestForms(unittest.TestCase):
    def test_form_1(self):
        browser.get(LINK_1)
        input_1 = browser.find_element_by_class_name("form-control.first").send_keys("John")
        input_2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input").send_keys("Doe")
        input_3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input").send_keys("abc123@gmail.com")
        button_1 = browser.find_element_by_css_selector("button.btn").click

        time.sleep(3)
        # browser.quit()
        assert input_2 == input_2, "NoSuchElementException "

    def test_form_2(self):
        browser.get(LINK_2)
        input1 = browser.find_element_by_class_name("form-control.first").send_keys("John")
        input2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input").send_keys("Doe")
        input3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input").send_keys("abc123@gmail.com")
        button = browser.find_element_by_css_selector("button.btn").click()
        time.sleep(3)
        browser.quit()
        assert input2 == input2, "NoSuchElementException"


if __name__ == "__main__":
    unittest.main()
