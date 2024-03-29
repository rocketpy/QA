# create a file with name test_web_page.py
# to run test, input in cmd:  pipenv run python -m pytest

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    
    
def test_basic_duckduckgo_search(browser):
    URL = 'https://www.duckduckgo.com'
    PHRASE = 'ford'
    browser.get(URL)
    search_input = browser.find_element_by_id('search_form_input_homepage')
    search_input.send_keys(PHRASE + Keys.RETURN)
    link_divs = browser.find_elements_by_css_selector('#links > div')
    assert len(link_divs) > 0
    xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
    phrase_results = browser.find_elements_by_xpath(xpath)
    assert len(phrase_results) > 0
    search_input = browser.find_element_by_id('search_form_input')
    assert search_input.get_attribute('value') == PHRASE

    
