#  in this example we separeting a tests, to smoke и regression parts  !!!

# to run a file with tests:  pytest -s -v -m smoke test_example.py
#  -m , use for marks
#  -v , verbose info


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

    @pytest.mark.smoke  # smoke , it's just a name (we can use any name but this name need add to registration file: pytest.ini) !!!
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression  # regression , it's just a name , we can use any name for marks
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
