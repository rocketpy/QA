from treq import get
# import treq


def done(response):
    print(response.code)
    reactor.stop()
    
# treq.get("https://github.com").addCallback(done) 
get("http://www...").addCallback(done)


from twisted.internet import reactor

reactor.run() 
# 200

# Example of Stress test script
import random  
from datetime import datetime
from twisted.internet import epollreactor  
epollreactor.install()
from twisted.internet import reactor, task  
from twisted.web.client import HTTPConnectionPool  
import treq
    

req_made = 0  
req_done = 0
req_generated = 0  
cooperator = task.Cooperator()
pool = HTTPConnectionPool(reactor)
    
def counter():  
