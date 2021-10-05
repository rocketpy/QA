# WebUI/HTTP automation testing framework based on unittest.

# PyPi: https://pypi.org/project/seldom/2.2.4/
# Github: https://github.com/SeldomQA/seldom

# pip install seldom==2.2.4
# or
# pip install -U git+https://github.com/SeldomQA/seldom.git@master


# Quick Start

# seldom -h
# usage: seldom [-h] [-v] [-project PROJECT] [-r R] [-m M] [-install INSTALL]

# WebUI automation testing framework based on Selenium.
"""
optional arguments:
  -h, --help        show this help message and exit
  -v, --version     show version
  -project PROJECT  Create an Seldom automation test project.
  -r R              run test case
  -m M              run tests modules, classes or even individual test methods
                    from the command line
  -install INSTALL  Install the browser driver, For example, 'chrome',
                    'firefox'.
"""

# Simple Example
import seldom


class BaiduTest(seldom.TestCase):
    def test_case(self):
        self.open("https://www.baidu.com")
        self.type(id_="kw", text="seldom")
        self.click(css="#su")
        self.assertTitle("seldom")


if __name__ == '__main__':
    seldom.main()

