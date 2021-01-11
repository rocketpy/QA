#  Postpython is a library for Postman that run Postman's collections

# Docs: https://github.com/k3rn3l-p4n1c/postpython

# pip install postpython

from postpython.core import PostPython


runner = PostPython('/path/to/collection/Postman echo.postman_collection')

response = runner.RequestMethods.get_request()

print(response.json())
print(response.status_code)

#  In Postpython you can assign values to environment variables in runtime
runner.environments.update({'BASE_URL': 'http://127.0.0.1:5000'})
runner.environments.update({'PASSWORD': 'test', 'EMAIL': 'you@email.com'})
