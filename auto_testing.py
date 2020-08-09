#  pip install seleniumbas
from seleniumbase import BaseCase


class MyTestClass(BaseCase):
    
    def test_my_site(self):
        self.demo_mode = True
        
