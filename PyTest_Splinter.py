# PyTest_Splinter - Splinter plugin for pytest testing framework

# PyPi: https://pypi.org/project/pytest-splinter/
# Github: https://github.com/pytest-dev/pytest-splinter

# pip install pytest-splinter

"""
Fixtures:
    browser:
        Get the splinter’s Browser. Fixture is underneath session scoped, so browser process is started once per test session,
        but the state of the browser will be clean (current page is blank, cookies clean).
    session_browser:
        The same as browser except the lifetime. This fixture is session-scoped so will only be finalized at the end of the whole test session.
        Useful if you want to speedup your test suite paying with reduced test isolation.
    browser_instance_getter:
        Function to create an instance of the browser.
        This fixture is required only if you need to have multiple instances of the Browser in a single test at the same time. Example of usage.
"""

@pytest.fixture
def admin_browser(request, browser_instance_getter):
    """Admin browser fixture."""
    # browser_instance_getter function receives parent fixture -- our admin_browser
    return browser_instance_getter(request, admin_browser)

def test_2_browsers(browser, admin_browser):
    """Test using 2 browsers at the same time."""
    browser.visit('http://google.com')
    admin_browser.visit('http://admin.example.com')


