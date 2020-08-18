#  docs about Skip and xfail:  https://docs.pytest.org/en/latest/skipping.html
#  for to mark some test like 'failed' and passing him , need use:  @pytest.mark.xfail 

#  when bug will be fixed , in console we will see: XPASS - 'unexpectedly passing' , after this need remove @pytest.mark.xfail

#  for run test file use: pytest -v test_file_name.py

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

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.xfail  # ths test is failed but we passing him
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")
        
    """
    #  when we use 'reason' , need use command:  pytest -rx -v test_file_name.py
    
    @pytest.mark.xfail(reason="fixing this bug right now")  #  here we added parameter: reason
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")
    """
