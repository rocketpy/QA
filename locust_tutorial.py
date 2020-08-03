#  Locust ia an open source load testing tool
#  DOCS:  https://docs.locust.io/en/stable/

#  pip install locust

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

    
