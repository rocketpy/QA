#  Poium - Selenium/appium-based Page Objects test library.

# PyPi: https://pypi.org/project/poium/
# Github: https://github.com/SeldomQA/poium

# pip install poium

# To keep up with the latest version:
# pip install -U git+https://github.com/SeldomQA/poium.git@master

# Example
from poium import Page, Element
from selenium import webdriver


class BaiduIndexPage(Page):
    search_input = Element(name='wd')
    search_button = Element(id_='su')


driver = webdriver.Chrome()
page = BaiduIndexPage(driver)
page.get("https://www.baidu.com")

page.search_input.send_keys("poium") 
page.search_button.click()

driver.quit()

