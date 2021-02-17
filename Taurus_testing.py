#  Taurus Tool for Continuous Testing , Automation-friendly framework for Continuous Testing !


#  PyPi:  https://pypi.org/project/bzt/
#  Docs:  https://gettaurus.org/docs/Index/

#  pip install bzt

#  Example for Locust , use locust.py
from locust import HttpUser, TaskSet, task, between
 
  
class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.post("/login", {"username": "test_user",
                                    "password": ""
                                   })
 
    @task
    def index(self):
        self.client.get("/")
 
    @task
    def about(self):
        self.client.get("/about/")
 

class WebsiteUser(HttpUser):
    tasks = [WebsiteTasks]
    wait_time = between(0.100, 1.500)


