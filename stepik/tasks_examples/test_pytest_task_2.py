import time
import math
import pytest
from selenium import webdriver


LINKS = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1']


@pytest.fixture(scope="class")
def driver_def():
    print("\nStart browser for test..")
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    print("\nQuit browser..")
    driver.quit()


class TestMainPage:
    @pytest.mark.parametrize('link', LINKS)
    def test_(self, driver, link):
        lnk = f"{link}"
        driver.get(lnk)
        driver.implicitly_wait(5)
        answer = math.log(int(time.time()))
        driver.browser.find_element_by_xpath("//*[@id='ember94']").send_keys(answer)
        driver.find_element_by_class_name("submit-submission").click()
        result = driver.find_element_by_xpath("//*[@id='ember122']/pre").text
        assert result == "Correct!", "Should be absolute value of a number"
        # print(result)
