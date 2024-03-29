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

# username = InputText(By.ID, 'username')

# Check if the element is enabled
enabled = username.web_element.is_enabled()

# Parent

form = PageElement(By.XPATH, "//form[@id='login']")
login_button = Button(By.XPATH, "./button", parent=form)

# Shadowroot
login_button = Button(By.CSS_SELECTOR, "css_selector", shadowroot="shadowroot_css_selector")

# webview_context_selection_callback:
login_button = Button(By.XPATH, "//*[@data-qsysid='subscription-counters']/div/div/", webview=True,
                      webview_context_selection_callback = webview_context_selector_per_url,
                      webview_csc_args = [driver_wrapper, WebviewConfigHelper.get_helper().account])


#  Group is a page element that contains other child page elements
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import InputText, Button, Group


class Form(Group):
    username = InputText(By.ID, 'username')
    password = InputText(By.ID, 'password')
    login_button = Button(By.XPATH, "./button")

class LoginPageObject(PageObject):
    form = Form(By.XPATH, "//form[@id='login']")

    def login(self, username, password):
        self.form.username.text = username
        self.form.password.text = password
        self.form.login_button.click()


# multiple page elements
inputs = InputTexts(By.XPATH, '//input')

for input in inputs.page_elements:
    input.clear()
    
    
# Concurrency issues
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import InputText, Button

class LoginPageObject(PageObject):
    def init_page_elements(self):
        self.username = InputText(By.ID, 'username')
        self.password = InputText(By.ID, 'password')
        self.login_button = Button(By.XPATH, "//form[@id='login']/button")

    def login(self, username, password):
        self.username.text = username
        self.password.text = password
        self.login_button.click()
