#  mechanize - Automate interaction with HTTP web servers

# PyPi:https://pypi.org/project/mechanize/
# Github: https://github.com/python-mechanize/mechanize
# Docs: https://mechanize.readthedocs.io/en/latest/

# pip install mechanize

"""
Major features:

Stateful programmatic web browsing in Python
  The browser class mechanize.Browser implements the interface of urllib2.OpenerDirector, so any URL can be opened not just http.
  Easy HTML form filling.
  Convenient link parsing and following.
  Browser history (.back() and .reload() methods).
  The Referer HTTP header is added properly (optional).
  Automatic observance of robots.txt.
  Automatic handling of HTTP-Equiv and Refresh.
"""

# Quickstart

import re
import mechanize


br = mechanize.Browser()
br.open("http://www.example.com/")

# follow second link with element text matching regular expression
response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)

print(br.title())
print(response1.geturl())
print(response1.info())  # headers
print(response1.read())  # body

