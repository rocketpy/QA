from selenium import webdriver
# from selenium.webdriver.support.ui import Select


LINK = ""

browser = webdriver.Chrome()
browser.get(LINK)

browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("option:nth-child(2)").click()  
#  or
browser.find_element_by_css_selector("[value='1']").click()

# or by Select , it's a best practice !
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") 

# Select by visible text
select.select_by_visible_text("text")

#  Select by index
elect.select_by_index(index)  # first index is 0


browser.quit()
