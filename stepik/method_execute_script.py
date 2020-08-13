from selenium import webdriver


browser = webdriver.Chrome()

# make a simple example with alert on web page
browser.execute_script("alert('Robots at work');")
#  or
browser.execute_script("document.title='Script executing';")

# two and more commands in one
browser.execute_script("document.title='Script executing';alert('Robots at work');")  # change title and call alert
