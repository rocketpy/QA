# Pytest-mock:  Thin-wrapper around the mock package for easier use with pytest

# PyPi:  https://pypi.org/project/pytest-mock/
# Github: https://github.com/pytest-dev/pytest-mock/

# pip install pytest-mock


# Usage
# The mocker fixture has the same API as mock.patch, supporting the same arguments:

def test_foo(mocker):
    # all valid calls
    mocker.patch('os.remove')
    mocker.patch.object(os, 'listdir', autospec=True)
    mocked_isfile = mocker.patch('os.path.isfile')

