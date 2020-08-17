#  for scopes we can use :  “function”, “class”, “module”, “session”

import pytest
from selenium import webdriver


link = "http://selenium1py.pythonanywhere.com/"

#  best practice use new browser for every one test !!!

@pytest.fixture(scope="class")  # here we use scope = class, one time per one class !!!
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    
@pytest.fixture(autouse=True)  #  autouse=True , it means , fixture need use for every one test BE CAREFUL with this !!!
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test2")
