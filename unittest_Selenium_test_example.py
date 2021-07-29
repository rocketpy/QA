import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class Register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/chromedriver")
        self.driver.maximize_window()

