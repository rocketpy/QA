# Playwright - A high-level API to automate web browsers

# PyPi:  https://pypi.org/project/playwright/
# pip install playwright

# Checking for sync API

# This is our default API for short snippets and tests. If you are not using asyncio in your application, it is the easiest to use Sync API notation.


from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch()
        page = browser.new_page()
        page.goto('http://whatsmyuseragent.org/')
        page.screenshot(path=f'example-{browser_type.name}.png')
        browser.close()


