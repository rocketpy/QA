# WebUI/HTTP automation testing framework based on unittest.

# PyPi: https://pypi.org/project/seldom/2.2.4/
# Github: https://github.com/SeldomQA/seldom

# Docs: https://seldomqa.readthedocs.io/en/latest/index.html

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
    
    
# HTTP
# seldom 2.0

import seldom


class TestRequest(seldom.TestCase):

    def test_put_method(self):
        self.put('/put', data={'key': 'value'})
        self.assertStatusCode(200)

    def test_post_method(self):
        self.post('/post', data={'key':'value'})
        self.assertStatusCode(200)

    def test_get_method(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        self.get("/get", params=payload)
        self.assertStatusCode(200)

    def test_delete_method(self):
        self.delete('/delete')
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(base_url="http://httpbin.org")
    
    
# Run the test
import seldom

seldom.main()
seldom.main(path="./")
seldom.main(path="./test_dir/")
seldom.main(path="./test_dir/test_sample.py")



