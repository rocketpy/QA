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

# Examples:
# Configure Mypy typings for auto-completion

# test_my_application.pyfrom playwright.sync_api import Page
def test_visit_admin_dashboard(page: Page):
    page.goto("/admin")
    # ...
    
# Configure slow mo#
# Run tests with slow mo with the --slowmo argument.

# pytest --slowmo 100
