# Selene - User-oriented Web UI browser tests in Python 

# Github: https://github.com/yashaka/selene

# Install latest stable version:
# pip install selene

# from sources
# GIVEN webdriver and webdriver_manager are already installed
$ git clone https://github.com/yashaka/selene.git
$ python setup.py install
# or using pip:
$ pip install git+https://github.com/yashaka/selene.git

"""
Main features:
    User-oriented API for Selenium Webdriver (code like speak common English)
    Ajax support (Smart implicit waiting and retry mechanism)
    PageObjects support (all elements are lazy-evaluated objects)
    Automatic driver management (no need to install and setup driver for quick local execution)
"""

# One more Example: https://github.com/yashaka/python-web-test

# Quick Start
from selene.support.shared import browser
from selene import by, be, have


browser.open('https://google.com/ncr')
browser.element(by.name('q')).should(be.blank)\
    .type('selenium').press_enter()
browser.all('.srg .g').should(have.size(10))\
    .first.should(have.text('Selenium automates browsers'))


# with custom setup
from selene.support.shared import browser
from selene import by, be, have


browser.config.browser_name = 'firefox'
browser.config.base_url = 'https://google.com'
browser.config.timeout = 2
# browser.config.* = ...

browser.open('/ncr')
browser.element(by.name('q')).should(be.blank)\
    .type('selenium').press_enter()
browser.all('.srg .g').should(have.size(10))\
    .first.should(have.text('Selenium automates browsers'))

