# Selene - User-oriented Web UI browser tests in Python 

# Github: https://github.com/yashaka/selene

"""
Main features:
    User-oriented API for Selenium Webdriver (code like speak common English)
    Ajax support (Smart implicit waiting and retry mechanism)
    PageObjects support (all elements are lazy-evaluated objects)
    Automatic driver management (no need to install and setup driver for quick local execution)
"""

# Quick Start
from selene.support.shared import browser
from selene import by, be, have

browser.open('https://google.com/ncr')
browser.element(by.name('q')).should(be.blank)\
    .type('selenium').press_enter()
browser.all('.srg .g').should(have.size(10))\
    .first.should(have.text('Selenium automates browsers'))
