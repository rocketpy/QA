#  for skip some test using : @pytest.mark.skip  , NO NEED add this to pytest.ini file  

import pytest
from selenium import webdriver


link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.skip  # this test will be skiped
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):  # this test will be passed
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
