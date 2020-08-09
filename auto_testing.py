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
                            
