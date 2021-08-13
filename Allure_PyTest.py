# Main steps:
# Allure Commandline:  https://docs.qameta.io/allure/
# Download the latest version as zip archive from https://github.com/allure-framework/allure-core/releases/latest
# Unpack the archive to allure-commandline directory.
# Navigate to bin directory.
# Use allure.bat for Windows and allure for other Unix platforms.

# Allure-Python:  https://github.com/allure-framework/allure-python

#  Install allure-adaptor for pytest
# pip install pytest-allure-adaptor

# Usage
# py.test --alluredir [path_to_report_dir]
# allure generate directory-with-results/


import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

@allure.feature('Functional testing')
@allure.story('Checking that the amount we entered has been used')
class TestCalculatorMoneyCurrency:
    @allure.step('Launch the Chrome browser, open and load the calculator page.')
    def setup_method(self, method):
        driver.maximize_window()
        driver.get('http://www...')
        assert 'Foreign currency calculator ' in driver.title
        driver.implicitly_wait(15)

        
    @allure.step('Resetting, closing the browser.')
    def teardown_method(self, method):
        driver.quit()

        
    @allure.step('Entering valid data in the amount input field and checking the result. ')
    def test_input_amount(self):

            amount = ['1', '1 250', '999 999 999 999', '3 600,57', '666 745,95']  # valid data list
            input_amount_field = driver.find_element_by_xpath("//input[@data-reactid='.0.$1.$0.0.1.0.0.0']")
            input_amount_field.click()

            for option in amount:
                input_amount_field.clear()
                input_amount_field.send_keys(option)
                button_convert = driver.find_element_by_xpath("//button[@data-reactid='.0.$1.$0.6.0']").click()

                with allure.step('Conversion result'):
                    assert driver.find_element_by_xpath("//div[@class='converter-result' and @data-reactid='.0.$1.$1']"), 'Conversion failed !' 

                    time.sleep(1)
                    num1 = driver.find_element_by_xpath("//span[@data-reactid='.0.$1.$1.1.0']").text
                    val1 = driver.find_element_by_xpath("//span[@data-reactid='.0.$1.$1.1.1']").text
                    #option = option + ',00'  # add the decimal part 
                    if ',' not in option:
                        option = option + ',00'

                    with allure.step('Compare the entered amount with the displayed result.'):
                        assert option == num1, 'The amounts do not match.'
                        
