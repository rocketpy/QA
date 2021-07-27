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
