#  Python client for Appium
#  Official website:  http://appium.io/
#  PyPi:  https://pypi.org/project/Appium-Python-Client/

#  pip install Appium-Python-Client

# Android environment
import unittest
from appium import webdriver


desired_caps = dict(platformName = 'Android'
                    platformVersion = '10'
                    automationName = 'uiautomator2'
                    deviceName = 'Android Emulator'
                    app = PATH('../../../apps/selendroid-test-app.apk')
                    )
self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
el = self.driver.find_element_by_accessibility_id('item')
el.click()


# iOS environment
import unittest
from appium import webdriver


desired_caps = dict(platformName = 'iOS'
                    platformVersion = '13.4'
                    automationName = 'xcuitest'
                    deviceName = 'iPhone Simulator'
                    app = PATH('../../apps/UICatalog.app.zip')
                    )

self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
el = self.driver.find_element_by_accessibility_id('item')
el.click()


import unittest
from appium import webdriver


desired_caps = dict(platformName = 'iOS'
                    platformVersion = '13.4'
                    automationName = 'xcuitest'
                    deviceName = 'iPhone Simulator'
                    app = PATH('../../apps/UICatalog.app.zip')
                    )

self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps, direct_connection=True)


# find element in appium using text
# driver.find_elements_by_xpath("//*[contains(text(), 'Submit')]")


