from treq import get


def done(response):
    print(response.code)
    reactor.stop()
    
get("http://www...").addCallback(done)


from twisted.internet import reactor

reactor.run() 
# 200
