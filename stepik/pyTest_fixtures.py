#  docs:  https://docs.pytest.org/en/latest/fixture.html

#  фикстуры, описанные в файле conftest.py в корневой директории проекта, могут вызываться в любом другом файле с тестами !!!

#  use command to run file :  pytest -s pyTest_fixtures.py
#  flag -s  need for show info from print()  in console

from selenium import webdriver


link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:

    @classmethod
    def setup_class(cls):  # cls
        print("\nstart browser for test suite..")
        cls.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):  # cls
        print("quit browser for test suite..")
        cls.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):  
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
