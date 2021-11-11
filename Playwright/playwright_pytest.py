# Pytest plugin for Playwright, a pytest wrapper with fixtures for Playwright to automate web browsers

# PyPi: https://pypi.org/project/pytest-playwright/
# Github: https://github.com/microsoft/playwright-pytest
# Docs: https://playwright.dev/python/docs/test-runners/


# pip install pytest-playwright

# Usage#

# pip install pytest-playwright

Use the page fixture to write a basic test. See more examples.

# test_my_application.pydef test_example_is_working(page):
# page.goto("https://example.com")    assert page.inner_text('h1') == 'Example Domain'    page.click("text=More information")

# To run your tests, use pytest CLI.

# Run tests (Chromium and headless by default)pytest
# Run tests in headed modepytest --headed
# Run tests in a different browser (chromium, firefox, webkit)pytest --browser firefox
# Run tests in multiple browserspytest --browser chromium --browser webkit


#  CLI arguments

    --headed: Run tests in headed mode (default: headless).
    --browser: Run tests in a different browser chromium, firefox, or webkit. It can be specified multiple times (default: all browsers).
    --browser-channel Browser channel to be used.
    --slowmo Run tests with slow mo.
    --device Device to be emulated.
    --output Directory for artifacts produced by tests (default: test-results).
    --tracing Whether to record a trace for each test. on, off, or retain-on-failure (default: off).
    --video Whether to record video for each test. on, off, or retain-on-failure (default: off).
    --screenshot Whether to automatically capture a screenshot after each test. on, off, or only-on-failure (default: off).

    
# Examples:
# Configure Mypy typings for auto-completion

# test_my_application.pyfrom playwright.sync_api import Page
def test_visit_admin_dashboard(page: Page):
    page.goto("/admin")
    # ...
    
# Configure slow mo#
# Run tests with slow mo with the --slowmo argument.

# pytest --slowmo 100


# Skip test by browser

# test_my_application.pyimport pytest
@pytest.mark.skip_browser("firefox")
def test_visit_example(page):
    page.goto("https://example.com")
    # ...
