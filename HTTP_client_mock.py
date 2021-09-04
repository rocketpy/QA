# httpretty - HTTP client mock for Python

# PyPi: https://pypi.org/project/httpretty/
# Docs: https://httpretty.readthedocs.io/en/latest/

# pip install httpretty

"""
Common Use Cases:
1. Test-driven development of API integrations
2. Fake responses of external APIs
3. Record and playback HTTP requests
"""

import sure
import httpretty
import requests


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_httpbin():
    httpretty.register_uri(
        httpretty.GET,
        "https://httpbin.org/ip",
        body='{"origin": "127.0.0.1"}'
    )

    response = requests.get('https://httpbin.org/ip')
    response.json().should.equal({'origin': '127.0.0.1'})

    httpretty.latest_requests().should.have.length_of(1)
    httpretty.last_request().should.equal(httpretty.latest_requests()[0])
    httpretty.last_request().body.should.equal('{"origin": "127.0.0.1"}')
    
