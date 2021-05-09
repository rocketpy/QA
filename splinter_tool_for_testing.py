#  browser abstraction for web acceptance testing and python tool for testing web applications


#  Github:  https://github.com/cobrateam/splinter
#  PyPi:  https://pypi.org/project/splinter/
#  pip install splinter

from splinter import Browser

browser = Browser()
browser.visit('http://...')
browser.fill('q', 'splinter - python acceptance testing for web applications')
browser.find_by_name('btnG').click()

if browser.is_text_present('splinter.readthedocs.io'):
    print("Yes, the official website was found!")
else:
    print("No, it wasn't found... We need to improve our SEO techniques")

browser.quit()

