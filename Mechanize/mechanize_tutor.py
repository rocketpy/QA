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

br.select_form(name="order")
# Browser passes through unknown attributes (including methods)
# to the selected HTMLForm.
br["cheeses"] = ["mozzarella", "caerphilly"]  # (the method here is __setitem__)
# Submit current form.  Browser calls .close() on the current response on
# navigation, so this closes response1
response2 = br.submit()

# print currently selected form (don't call .submit() on this, use br.submit())
print(br.form)

response3 = br.back()  # back to cheese shop (same data as response1)
# the history mechanism returns cached response objects
# we can still use the response, even though it was .close()d
response3.get_data()  # like .seek(0) followed by .read()
response4 = br.reload()  # fetches from server

for form in br.forms():
    print(form)
# .links() optionally accepts the keyword args of .follow_/.find_link()
for link in br.links(url_regex="python.org"):
    print(link)
    br.follow_link(link)  # takes EITHER Link instance OR keyword args
    br.back()

# control the browser’s policy by using the methods of mechanize. Browser’s base class, mechanize.UserAgent.
# example:

br = mechanize.Browser()
# Explicitly configure proxies (Browser will attempt to set good defaults).
# Note the userinfo ("joe:password@") and port number (":3128") are optional.
br.set_proxies({"http": "joe:password@myproxy.example.com:3128",
                "ftp": "proxy.example.com",
                })

# Add HTTP Basic/Digest auth username and password for HTTP proxy access.

# (equivalent to using "joe:password@..." form above)
br.add_proxy_password("joe", "password")

# Add HTTP Basic/Digest auth username and password for website access.
br.add_password("http://example.com/protected/", "joe", "password")

# Add an extra header to all outgoing requests, you can also
# re-order or remove headers in this function.
br.finalize_request_headers = lambda request, headers: headers.__setitem__(
  'My-Custom-Header', 'Something')

# Don't handle HTTP-EQUIV headers (HTTP headers embedded in HTML).
br.set_handle_equiv(False)

# Ignore robots.txt.  Do not do this without thought and consideration.
br.set_handle_robots(False)

# Don't add Referer (sic) header
br.set_handle_referer(False)

# Don't handle Refresh redirections
br.set_handle_refresh(False)

# Don't handle cookies
br.set_cookiejar()
# Supply your own mechanize.CookieJar (NOTE: cookie handling is ON by
# default: no need to do this unless you have some reason to use a
# particular cookiejar)
br.set_cookiejar(cj)
# Tell the browser to send the Accept-Encoding: gzip header to the server
# to indicate it supports gzip Content-Encoding
br.set_request_gzip(True)
# Do not verify SSL certificates
