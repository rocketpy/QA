#  this plugin using for retesting a failed some test 

#  pip install pytest-rerunfailures==7.0

#  IMPORTANT
#  pytest -v --tb=line --reruns 1 --browser_name=chrome test_file_name.py  , this is example a command
#  --reruns 1 , is how many times need rerun a failed tests
#  --tb=line , is a make shortly log


#  simple example
"""
link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")
    
#  result is "1 failed, 1 passed, 1 rerun in 9.20s"
"""
