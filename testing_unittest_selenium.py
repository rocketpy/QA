import unittest
import requests
from selenium import webdriver


#  taked from:  https://help.crossbrowsertesting.com/selenium-testing/getting-started/python/

class SeleniumCBT(unittest.TestCase):
    def setUp(self):

        self.username = "user@email.com"  # need be sign_in in https://crossbrowsertesting.com/
        self.authkey  = "secret_key"  # need be sign_in in https://crossbrowsertesting.com/

        self.api_session = requests.Session()
        self.api_session.auth = (self.username,self.authkey)
        self.test_result = None

        caps = {}
        caps['browserName'] = 'Chrome'
        caps['version'] = '60x64'
        caps['platform'] = 'Windows 10'
        caps['screenResolution'] = '1366x768'
        caps['record_video'] = 'true'

        self.driver = webdriver.Remote(desired_capabilities=caps,
                                       command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username, self.authkey)
                                      )
        
        self.driver.implicitly_wait(20)

    def test_CBT(self):
            self.driver.get('http://crossbrowsertesting.github.io/selenium_example_page.html')
            self.assertEqual("Selenium Test Example Page", self.driver.title)
            self.test_result = 'pass'
            self.driver.quit()
       

if __name__ == '__main__':
    unittest.main()

    
#  basic example by unittest (taked from : https://docs.python.org/2.7/library/unittest.html)
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

    
#  running tests in Parallel
from queue import Queue
from threading import Thread
from selenium import webdriver
import time


USERNAME = "user@email.com"
API_KEY = "12345"

q = Queue(maxsize=0)

browsers = [
  {"os_api_name": "Win7x64-C2", "browser_api_name": "IE10", "name": "Python Parallel"},
  {"os_api_name": "Win8.1", "browser_api_name": "Chrome43x64", "name": "Python Parallel"},
]

# put all of the browsers into the queue before pooling workers
for browser in browsers:
    q.put(browser)

num_threads = 10

def test_runner(q):
    while q.empty() is False:
        try:
            browser = q.get()
            print("%s: Starting" % browser["browser_api_name"])
            driver = webdriver.Remote(desired_capabilities=browser, command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (USERNAME, API_KEY) )
            print("%s: Getting page" % browser["browser_api_name"])
            driver.get("http://crossbrowsertesting.com")
            print("%s: Quitting browser and ending test" % browser["browser_api_name"])
        except:
            print("%s: Error" % browser["browser_api_name"])
        finally:                    
            driver.quit()
            time.sleep(15)
            q.task_done()
