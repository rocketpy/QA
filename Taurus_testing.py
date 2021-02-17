#  Taurus Tool for Continuous Testing , Automation-friendly framework for Continuous Testing !


#  PyPi:  https://pypi.org/project/bzt/
#  Docs:  https://gettaurus.org/docs/Index/

#  pip install bzt

#  Get started:
#  Create a file named test.yml with following contents:
"""
---
execution:
- concurrency: 10
  ramp-up: 1m
  hold-for: 1m30s
  scenario: simple
  
scenarios:
  simple:
    think-time: 0.75
    requests:
    - http://blazedemo.com/
    - http://blazedemo.com/vacation.html
"""
#  Then run bzt test.yml


#  Example for Locust , use locust.py
#  pip install locustio
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
   
   
#  example config that uses existing locust file:   YAML
"""
execution:
- executor: locust
  concurrency: 10
  ramp-up: 1m
  iterations: 1000
  scenario: example

scenarios:
  example:
    default-address: http://blazedemo.com
    script: sample.py
"""

# For more information go to:  https://gettaurus.org/docs/Locust/

