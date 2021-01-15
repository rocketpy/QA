#  create a file called locustfile.py 
from locust import HttpLocust, TaskSet, task


# /home/<your user>/.local/bin/locust --host=http://<host-to-test>
# or
# locust --host=http://<host-to-test>   ,if you have installed locust system-wide
#  open http://localhost:8089/ in your browser

class LoginWithUniqueUser(TaskSet):
    @task
    def login(self):
        self.client.post("/login", {
            'email': 'User1@gmail.com', 'password': '1234567890'
        })

        
class LoginWithUniqueUserTest(HttpLocust):
    task_set = LoginWithUniqueUsersSteps
    host = "http://"
    sock = None

    def __init__(self):
        super(LoginWithUniqueUserTest, self).__init__()        
        
        
#  make a simple request GET , create a file called locustfile.py        
from locust import HttpLocust, TaskSet, task, between


# /home/<your user>/.local/bin/locust --host=http://<host-to-test>
# or
# locust --host=http://<host-to-test>   ,if you have installed locust system-wide
#  open http://localhost:8089/ in your browser

class UserBehaviour(TaskSet):  # class UserBehaviour is a collection of the actions these users do
    @task
    def getFrontPage(self):
        self.client.get("/")

class User(HttpLocust):  # class User represents users of your app
    task_set = UserBehaviour
    wait_time = between(1, 10)
    
     
