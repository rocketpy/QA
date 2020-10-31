from locust import HttpLocust, TaskSet, task


#  FOR RUN TEST  USE:  locust -f locust_files/my_locust_file.py --host=http://example.com

class UserBehavior(TaskSet):
    def on_start(self):
        pass  # add code that you want to run during ramp up

    def on_stop(self):
        pass  # add code that you want to run during ramp down

    def registration(self):
        name = fake.first_name()
        last_name = fake.last_name()
        password = ''
        email = name + last_name + '@gmail.com'
        phone = fake.phone_number()
        URL = "ip"
        PARAMS = {'name':name,'password': password,'primary_email': email,'primary_mobile_number':phone,'country_abbrev':'US'} 
        self.client.post(URL, PARAMS)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
    
    
#  OR

from locust import HttpLocust, TaskSet


"""
To start the load test, run locust -f locust_files/my_locust_file.py --host=http://example.com 
where host would be your IP. You can then go to 127.0.0.1:8089 to select the number of virtual users to simulate.
On windows there's a limitation of 1024 users only.
"""

def login(self):
    params= {'name':'test','password':'test1','primary_email':'test667@gmail.com','primary_mobile_number':'9999999999','country_abbrev':'US'}
    self.client.post(URL, data=params)
    # The data parameter or json can both be used here. If it's a dict then data would work but for json replace data with json.
    # For more information you can check out requests package as Locust internally uses requests only.

    
class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1}

    def on_start(self):
        login(self)

    def on_stop(self):
        pass

    @task
    def try(self):
       pass

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000    

"""
#  for uniques user use module Faker

def registration:
    URL = "ip"
    PARAMS = {'name':'test','password':'test1','primary_email':'test667@gmail.com','primary_mobile_number':'9999999999','country_abbrev':'US'} 
    r = requests.post(url = URL,params = PARAMS, auth=HTTPDigestAuth('user', 'pass')) 
    response = r.text 
    print response
"""
