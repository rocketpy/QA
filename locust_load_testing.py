#  If named the file as anything other than locustfile.py then you need pass the file name when you start locust !!! so need use locustfile.py

#  task_set attribute - should point to a TaskSet class which defines the behaviour of the user - 
#  - атрибут task_set - должен указывать на класс TaskSet, который определяет поведение пользователя.

#  wait_time attribute - how long a simulated user will wait between executing tasks -
#  - атрибут wait_time - как долго моделируемый пользователь будет ждать между выполнением задач


from locust import constant, TaskSet
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
        response = self.client.get(self.api_path)
        
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

