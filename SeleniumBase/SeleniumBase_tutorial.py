# SeleniumBase - A complete web automation framework for end-to-end testing.

# PyPi: https://pypi.org/project/seleniumbase/
# Github: https://github.com/seleniumbase/SeleniumBase

# Install SeleniumBase:

# from GitHub:
# git clone https://github.com/seleniumbase/SeleniumBase.git
# cd SeleniumBase/
# pip install .  # Normal installation
# pip install -e .  # Editable install

# (When using a virtual env, the Editable install is faster.)

# from pypi:
# pip install seleniumbase


from seleniumbase import BaseCase


class MyTestClass(BaseCase):
    def test_basics(self):
        url = "https://store.xkcd.com/collections/posters"
        self.open(url)
        self.type('input[name="q"]', "xkcd book")
        self.click('input[value="Search"]')
        self.assert_text("xkcd: volume 0", "h3")
        self.open("https://xkcd.com/353/")
        self.assert_title("xkcd: Python")
        self.assert_element('img[alt="Python"]')
        self.click('a[rel="license"]')
        self.assert_text("free to copy and reuse")
        self.go_back()
        self.click_link("About")
        self.assert_exact_text("xkcd.com", "h2")
