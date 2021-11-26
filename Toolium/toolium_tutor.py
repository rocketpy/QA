#  Toolium - Wrapper tool of Selenium and Appium libraries to test web and mobile applications in a single project

# PyPI: https://pypi.org/project/toolium/
# Github: https://github.com/telefonica/toolium

# pip install toolium
# or
# git clone git@github.com:Telefonica/toolium-template.git
# cd toolium-template
# pip install -r requirements.txt

# The main dependencies are:
    # Selenium: to test web applications in major browsers (Firefox, Chrome, Internet Explorer, Edge, Safari, Opera)
    # Appium-Python-Client: to test mobile applications (native, hybrid or web) in Android or iOS devices/emulators.
    # requests: to test APIs

    
#  Example of a page object definition:

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import InputText, Button


class LoginPageObject(PageObject):
    username = InputText(By.ID, 'username')
    password = InputText(By.ID, 'password')
    login_button = Button(By.XPATH, "//form[@id='login']/button")

    def login(self, username, password):
        self.username.text = username
        self.password.text = password
        self.login_button.click()
        

# Example of a test using the previous page object:

def test_login(self):
    LoginPageObject().login('user', 'pass')
    ...

#  Methods

username = InputText(By.ID, 'username')

# Get text value
input_value = username.text

# Set text value
username.text = 'username'
