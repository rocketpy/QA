# Python DSL for easily testing REST services

# PyPi: https://pypi.org/project/restpite/
# Github: https://github.com/symonk/restpite
# Docs: https://restpite.readthedocs.io/en/latest/installation.html

# pip install restpite
# git clone git://github.com/symonk/restpite

# Restpite API: https://restpite.readthedocs.io/en/latest/modules.html

"""
Features of restpite:
    Supports HTTP/1.1 & HTTP/2
    Client supports both sync and async to avoid needlessly blocking on IO operations like requests
    Extendable handler and hook dispatching system to allow client code to intercept HTTP flow
    Powerful in built assertions for everything imaginable on your response objects
    Integrates gracefully with marshmallow to easily deserialize response json into python objects
    Intuitive DSL, underpinned by the brilliant httpx library
    Automatic and customisable performance and request-response tracking in various formats
    Tons of other cool features
"""

