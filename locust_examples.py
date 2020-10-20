import requests
from locust import HttpLocust, TaskSet
from requests.auth import HTTPDigestAuth
from credentials import *


class UserBehavior(TaskSet):
    def on_start(self):
        if len(USER_CREDENTIALS) > 0:
                self.name, self.password,self.email,self.phone,self.country_abbrev = USER_CREDENTIALS.pop()
    @task
    def registration(self):
        URL = "ip/user/register"
        PARAMS = {'name':self.name,'password': self.password,'primary_email': self.email,'primary_mobile_number':self.phone,'country_abbrev':self.country_abbrev} 
        self.client.post(url = URL,params = PARAMS,auth=HTTPDigestAuth('user', 'pass'))

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
