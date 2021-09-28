#  Lighter browser automation based on Selenium.

# PyPi: https://pypi.org/project/helium/
# Github: https://github.com/mherrmann/selenium-python-helium

# Helium cheatsheet: https://github.com/mherrmann/selenium-python-helium/blob/master/docs/cheatsheet.md

# pip install helium

from helium import *


start_chrome()
# start_firefox()

# or
start_chrome('google.com'))

# headless
start_chrome(headless=True)
start_chrome('google.com', headless=True)
# same for Firefox

# Simple example
from helium import *


start_chrome('google.com')
write('helium selenium github')
press(ENTER)
click('mherrmann/helium')
go_to('github.com/login')
write('username', into='Username')
write('password', into='Password')
click('Sign in')
kill_browser()


