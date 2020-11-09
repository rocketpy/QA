from locust import HttpLocust, TaskSet, task


class LoginWithUniqueUser(TaskSet):
    @task
    def login(self):
        self.client.post("/login", {
            'email': 'User1@gmail.com', 'password': '123456'
        })
