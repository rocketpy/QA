#  How to change command line options

# content of pytest.ini
# addopts = -ra -q

"""
Alternatively, you can set a PYTEST_ADDOPTS environment variable to add command line options while the environment is in use:

export PYTEST_ADDOPTS="-v"

Here’s how the command-line is built in the presence of addopts or the environment variable:

<pytest.ini:addopts> $PYTEST_ADDOPTS <extra command-line arguments>
"""

# So if the user executes in the command-line:
#  pytest -m slow

# The actual command line executed is:
#  pytest -ra -q -v -m slow

# Note that as usual for other command-line applications, in case of conflicting options the last one wins,
# so the example above will show verbose output because -v overwrites -q.


#  Pass different values to a test function, depending on command line options
# Suppose we want to write a test that depends on a command line option. Here is a basic pattern to achieve this:

# content of test_sample.py
def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    assert 0  # to see what was printed

For this to work we need to add a command line option and provide the cmdopt through a fixture function:

# content of conftest.py
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

# run this without supplying our new option:
$ pytest -q test_sample.py


# Command line option arrived in our test.
# Add simple validation for the input by listing the choices:

# content of conftest.py
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt",
        action="store",
        default="type1",
        help="my option: type1 or type2",
        choices=("type1", "type2"),
    )

    
# get feedback on a bad argument:

$ pytest -q --cmdopt=type3
# ERROR: usage: pytest [options] [file_or_dir] [file_or_dir] [...]
# pytest: error: argument --cmdopt: invalid choice: 'type3' (choose from 'type1', 'type2')




