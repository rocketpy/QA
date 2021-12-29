#  Python client for Appium
#  Official website:  http://appium.io/
#  PyPi:  https://pypi.org/project/Appium-Python-Client/

#  pip install Appium-Python-Client

# Install from source via GitHub.
# git clone git@github.com:appium/python-client.git
# cd python-client
# python setup.py install


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

self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                               desired_caps, direct_connection=True)


# find element in appium using text
# driver.find_elements_by_xpath("//*[contains(text(), 'Submit')]")

#  find the location of elements
# self.driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys("XXXXX")
# or
# self.driver.find_element_by_xpath("//android.widget.EditText[@index='1']").send_keys("XXXXX")


#  For example, the below action builder is to replace the default one with the touch pointer action.
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder


actions = ActionChains(driver)
# override as 'touch' pointer action
actions.w3c_actions = ActionBuilder(driver,
                                    mouse=PointerInput(interaction.POINTER_TOUCH,
                                                       "touch"))
actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(2)
actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
actions.w3c_actions.pointer_action.release()
actions.perform()


#  Direct Connect URLs
"""
If your Selenium/Appium server decorates the new session capabilities response with the following keys:

    directConnectProtocol
    directConnectHost
    directConnectPort
    directConnectPath

Then python client will switch its endpoint to the one specified by the values of those keys.
"""

import unittest
from appium import webdriver


desired_caps = dict(
    platformName='iOS',
    platformVersion='13.4',
    automationName='xcuitest',
    deviceName='iPhone Simulator',
    app=PATH('../../apps/UICatalog.app.zip')
)

self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                               desired_caps, direct_connection=True)


