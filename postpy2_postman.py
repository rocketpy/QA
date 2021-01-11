#  Postpy2 is a library for Postman that run Postman's collections

# PyPi: https://pypi.org/project/postpy2/
# Docs: https://github.com/matkapi/postpy2

# pip install Postpy2

from Postpy2.core import Postpy2


runner = Postpy2('/path/to/collection/Postman echo.postman_collection')

response = runner.RequestMethods.get_request()

print(response.json())
print(response.status_code)

#  load enviromental variables from postman enviroment files
pp.environments.load('environments/test.postman_environment.json')

# assign values to environment variables in runtime
runner.environments.update({'BASE_URL': 'http://127.0.0.1:5000'})
runner.environments.update({'PASSWORD': 'test', 'EMAIL': 'you@email.com'})
