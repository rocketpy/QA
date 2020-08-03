#  Locust ia an open source load testing tool
#  DOCS:  https://docs.locust.io/en/stable/
#  Very Important :  JMeter(Java) running in GUI mode for the same scenario takes almost in 30x more memory than a Locust script !!!

#  Locust’s web interface - http://127.0.0.1:8089

#  without using the web interface, use --headless

#  pip install locust

# to start locust in master mode:  locust -f my_locustfile.py --master

#  run the test saved as locustfile.py , in the terminal:  locust --host=http://127.0.0.1:8000

#  creating a Performance Test 
from locust import HttpLocust, TaskSet, task


class LoginPage(TaskSet):
    @task
    def login_page_with_response_code_assertion(self):
        r = self.client.get("/login/")
        assert r.status_code is 200, "Unexpected response code: " + r.status_code
class LoginUser(HttpLocust):
    task_set = LoginPage
    host = "http://127.0.0.1:8000"
    min_wait = 1000
    max_wait = 5000

    
#  other example (from official website)
from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    def on_start(self):
        self.client.post("/login", {
            "username": "test_user",
            "password": ""
        })
    
    @task
    def index(self):
        self.client.get("/")
        self.client.get("/static/assets.js")
        
    @task
    def about(self):
        self.client.get("/about/")
        
        
# this example will simulate a user(from off. website)

import random
from locust import HttpUser, between, task
from pyquery import PyQuery


class AwesomeUser(HttpUser):
    host = "https://docs.locust.io/en/latest/"
    
    # we assume someone who is browsing the Locust docs, 
    # generally has a quite long waiting time (between 
    # 10 and 600 seconds), since there's a bunch of text 
    # on each page
    wait_time = between(10, 600)
    
    def on_start(self):
        # start by waiting so that the simulated users 
        # won't all arrive at the same time
        self.wait()
        # assume all users arrive at the index page
        self.index_page()
        self.urls_on_current_page = self.toc_urls
    
    @task(10)
    def index_page(self):
        r = self.client.get("")
        pq = PyQuery(r.content)
        link_elements = pq(".toctree-wrapper a.internal")
        self.toc_urls = [
            l.attrib["href"] for l in link_elements
        ]
    
    @task(50)
    def load_page(self):
        url = random.choice(self.toc_urls)
        r = self.client.get(url)
        pq = PyQuery(r.content)
        link_elements = pq("a.internal")
        self.urls_on_current_page = [
            l.attrib["href"] for l in link_elements
        ]
    
    @task(30)
    def load_sub_page(self):
        url = random.choice(self.urls_on_current_page)
        r = self.client.get(url)
