# Pytest plugin for Playwright, a pytest wrapper with fixtures for Playwright to automate web browsers

# PyPi: https://pypi.org/project/pytest-playwright/
# Github: https://github.com/microsoft/playwright-pytest
# Docs: https://playwright.dev/python/docs/test-runners/


# pip install pytest-playwright

# Examples:
# Configure Mypy typings for auto-completion#

# test_my_application.pyfrom playwright.sync_api import Page
def test_visit_admin_dashboard(page: Page):
    page.goto("/admin")
    # ...
    
# Configure slow mo#
# Run tests with slow mo with the --slowmo argument.

# pytest --slowmo 100
