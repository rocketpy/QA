#  Locust ia an open source load testing tool
#  DOCS:  https://docs.locust.io/en/stable/
#  Very Important :  JMeter(Java) running in GUI mode for the same scenario takes almost in 30x more memory than a Locust script !!!

#  Locust’s web interface - http://127.0.0.1:8089

#  without using the web interface, use --headless

#  pip install locust

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
