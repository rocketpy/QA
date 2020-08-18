#  inversion - it means , run tests NOT for SMOKE use command:  pytest -s -v -m "not smoke" test_example.py

#  for united tests need use:  pytest -s -v -m "smoke or regression" test_example.py

#  for THIS example need use this command:  pytest -s -v -m "smoke and win10" test_file_name.py
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


class TestMainPage1(object):

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10  # here we added a new mark
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
