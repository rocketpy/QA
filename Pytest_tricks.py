#  How to change command line options

# content of pytest.ini
# addopts = -ra -q

"""
Alternatively, you can set a PYTEST_ADDOPTS environment variable to add command line options while the environment is in use:

export PYTEST_ADDOPTS="-v"

Here’s how the command-line is built in the presence of addopts or the environment variable:

<pytest.ini:addopts> $PYTEST_ADDOPTS <extra command-line arguments>
"""


