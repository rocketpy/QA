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
    PHRASE = 'panda'
    # Navigate to the DuckDuckGo home page
    browser.get(URL)
    # Find the search input element
    # In the DOM, it has an 'id' attribute of 'search_form_input_homepage'
    search_input = browser.find_element_by_id('search_form_input_homepage')
  # Send a search phrase to the input and hit the RETURN key
  search_input.send_keys(PHRASE + Keys.RETURN)
  # Verify that results appear on the results page
  link_divs = browser.find_elements_by_css_selector('#links > div')
  assert len(link_divs) > 0
  # Verify that at least one search result contains the search phrase
  xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
  phrase_results = browser.find_elements_by_xpath(xpath)
  assert len(phrase_results) > 0
  # Verify that the search phrase is the same
  search_input = browser.find_element_by_id('search_form_input')
  assert search_input.get_attribute('value') == PHRASE
