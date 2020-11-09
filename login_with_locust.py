from locust import HttpLocust, TaskSet, task


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
        
