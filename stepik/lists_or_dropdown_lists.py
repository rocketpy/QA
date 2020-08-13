from selenium import webdriver
# from selenium.webdriver.support.ui import Select


LINK = ""

browser = webdriver.Chrome()
browser.get(LINK)

browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("option:nth-child(2)").click()  
#  or
browser.find_element_by_css_selector("[value='1']").click()

# or by Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") 


browser.quit()
