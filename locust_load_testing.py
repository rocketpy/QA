#  If named the file as anything other than locustfile.py then you need pass the file name when you start locust !!! so need use locustfile.py

#  task_set attribute - should point to a TaskSet class which defines the behaviour of the user - 
#  - атрибут task_set - должен указывать на класс TaskSet, который определяет поведение пользователя.

#  wait_time attribute - how long a simulated user will wait between executing tasks -
#  - атрибут wait_time - как долго моделируемый пользователь будет ждать между выполнением задач

# IMPORTANT: to start locust without the Web UI and generate the results in csv output:  env API_TOKEN=<apiKey> locust --master --csv=results --no-web -c 200 -r 50 --host
# for this project use
# env API_TOKEN=<apiKey> locust --master --csv=results --no-web -c 200 -r 50 --host http://api.openweathermap.org

#  VERY  IMPORTANT   !!!!!
#  RUN the load test, recommended to run it in distributed mode. Locust in distributed mode has master and slaves.
#  MASTER node doesn’t simulate any users and just manages the Web UI.
#  IF our machine has 4 CPU cores, then we need to run one slave instance per processor core in the machine.

#  First, start the master node by running below command in the same location you have your locustfile:
#  env API_TOKEN=<apiKey> locust --master

#  Second, start up a number of slaves based on the cores in your machine:
#  locust --slave &
#  locust --slave &
#  locust --slave &
#  locust --slave &

#  You should have the Web UI running at http://localhost:8089/

# IMPORTANT: to start locust without the Web UI and generate the results in csv output:  env API_TOKEN=<apiKey> locust --master --csv=results --no-web -c 200 -r 50 --host
# for this project use
# env API_TOKEN=<apiKey> locust --master --csv=results --no-web -c 200 -r 50 --host http://api.openweathermap.org

import os
from locust import TaskSet, task, constant
from locust.contrib.fasthttp import FastHttpLocust  #  for making an HTTP request
from csvreader import CSVReader


reader = CSVReader("file_name.csv")  # or path to file


class MyLocust(FastHttpLocust):
    task_set = # TaskSet class
    wait_time = constant(0)

#  Есть несколько встроенных функций для определения времени ожидания, таких как between , constant и constant_pacing .

class MyTaskSet(TaskSet):
    api_path = "/data/2.5/weather?q={},{}&appid={}"

    @task
    def api_call(self):
        data = next(reader)
        response = self.client.get(self.api_path.format(data[0], data[1], os.environ.get("API_KEY")))        
        # response = self.client.get(self.api_path)
        
#  need create a new file csvreader.py with this code !!!
import csv


class CSVReader:
    def __init__(self, file):
        try:
            file = open(file)
        except TypeError:
            pass
        self.file = file
        self.reader = csv.reader(file)

    def __next__(self):
        try:
            return next(self.reader)
        except StopIteration:
            self.file.seek(0, 0)
            return next(self.reader)

