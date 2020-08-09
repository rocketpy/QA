#  docs: https://pypi.org/project/seleniumbase/

#  pip install seleniumbas

from seleniumbase import BaseCase


class MyTestClass(BaseCase):
    
    def test_my_site(self):
        self.demo_mode = True
        self.demo_sleep = 0.5
        self.message_duration = 2.5
        self.open("https://.../search/")
        
        title = "Bla bla bla"  # send_key
        
        self.type('[placeholder]', title + "\n")  # self.type(SELECTOR, TEXT)  # Type text (Add "\n" to text for pressing enter/return.)
        self.click("link=%s", title)
        self.assert_element("div.nav-content [id]")
        self.assert_text(title, "h1")
        self.highlight("div.description div.abstract")
        self.highlight("h2")
        
        h3 = "h3:nth-of-type(%s)" 
        
        self.assert_text('Some text ...', h3 % "1")
        self.assert_text('Some text ...', h3 % "2")
        self.assert_text('Some text ...', h3 % "3")
        self.assert_text('Some text ...', h3 % "4")
        self.assert_text('Some text ...', h3 % "5")
                            

            
"""
self.open(URL)  # Navigate to the web page
self.click(SELECTOR)  # Click a page element
self.type(SELECTOR, TEXT)  # Type text (Add "\n" to text for pressing enter/return.)
self.assert_element(SELECTOR)  # Assert element is visible
self.assert_text(TEXT)  # Assert text is visible (has optional SELECTOR arg)
self.assert_title(PAGE_TITLE)  # Assert page title
self.assert_no_404_errors()  # Assert no 404 errors from files on the page
self.assert_no_js_errors()  # Assert no JavaScript errors on the page (Chrome-ONLY)
self.execute_script(JAVASCRIPT)  # Execute javascript code
self.go_back()  # Navigate to the previous URL
self.get_text(SELECTOR)  # Get text from a selector
self.get_attribute(SELECTOR, ATTRIBUTE)  # Get a specific attribute from a selector
self.is_element_visible(SELECTOR)  # Determine if an element is visible on the page
self.is_text_visible(TEXT)  # Determine if text is visible on the page (optional SELECTOR)
self.hover_and_click(HOVER_SELECTOR, CLICK_SELECTOR)  # Mouseover element & click another
self.select_option_by_text(DROPDOWN_SELECTOR, OPTION_TEXT)  # Select a dropdown option
self.switch_to_frame(FRAME_NAME)  # Switch webdriver control to an iframe on the page
self.switch_to_default_content()  # Switch webdriver control out of the current iframe
self.switch_to_window(WINDOW_NUMBER)  # Switch to a different window/tab
self.save_screenshot(FILE_NAME)  # Save a screenshot of the current page
"""
