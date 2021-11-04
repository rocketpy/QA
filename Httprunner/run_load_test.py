# Run load test 

# Integrated since HttpRunner 3.1.0
# With reuse of Locust, you can run load test without extra work.

# $ locusts -V                                                                 
# locust 1.0.3

"""
For full usage, you can run locusts -h to see help, and you will find that it is the same with locust -h.

The only difference is the -f/--locustfile argument. When you specify -f with a YAML/JSON testcase file,
it will convert to pytest first and then run load test with HttpRunner's builtin locustfile(httprunner/ext/locust/locustfile.py).
"""
