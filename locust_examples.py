import requests
from locust import HttpLocust, TaskSet
from requests.auth import HTTPDigestAuth
from credentials import *


#  run locust -f locust.py --host=localhost:8089

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
    wait_time = between(5, 9)  # between 5 and 9 seconds

    
import requests
from locust import HttpLocust, TaskSet
from requests.auth import HTTPDigestAuth
from credentials import *    
    
    
class UserBehavior(TaskSet):

    def on_start(self):
    """ on_start is called when a Locust start before
        any task is scheduled
    """
    self.client.post("/resources/", json=RESOURCE_1, headers=headers_with_auth)

    @task(1)
    def profile(self):
        self.client.get("/resources/", json={})

class WebsiteUser(HttpLocust):
    def setup(self):
        client = clients.HttpSession(base_url=self.host)
        client.post("/resources/", json=RESOURCE_1, headers=headers_with_auth)
    task_set = UserBehavior
    wait_time = between(5, 9)  # between 5 and 9 seconds

    
