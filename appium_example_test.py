from appium import webdriver


desired_caps = {'platformName': 'iOS',
                'platformVersion': '11.1',
                'deviceName': 'iPhone SE',
                'app': '/Users/...app'
                }

def test_sum_two_integers():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.find_element_by_name('3').click()
    driver.find_element_by_name('+').click()
    driver.find_element_by_name('2').click()
    driver.find_element_by_name('=').click()
    numbers_field = driver.find_element_by_xpath('//TypeStaticText')
    assert int(numbers_field.text) == 5
    driver.quit()
