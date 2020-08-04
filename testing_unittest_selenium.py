import unittest
import requests
from selenium import webdriver


class SeleniumCBT(unittest.TestCase):
    def setUp(self):

        self.username = "user@email.com"
        self.authkey  = "secret_key"

        self.api_session = requests.Session()
        self.api_session.auth = (self.username,self.authkey)
        self.test_result = None

