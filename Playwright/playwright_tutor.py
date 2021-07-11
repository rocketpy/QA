# Playwright - A high-level API to automate web browsers

# PyPi:  https://pypi.org/project/playwright/
# pip install playwright

# PyTest and Playwright:  https://github.com/microsoft/playwright-pytest

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

        
# Async API

# If your app is based on the modern asyncio loop and you are used to async/await constructs,
# Playwright exposes Async API for you. You should use this API inside a Python REPL supporting asyncio like with python -m asyncio

# python -m asyncio
"""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto('http://whatsmyuseragent.org/')
            await page.screenshot(path=f'example-{browser_type.name}.png')
            await browser.close()

asyncio.run(main())
"""

# With pytest

# Use our pytest plugin for Playwright.

def test_playwright_is_visible_on_google(page):
    page.goto("https://www.google.com")
    page.type("input[name=q]", "Playwright GitHub")
    page.click("input[type=submit]")
    page.wait_for_selector("text=microsoft/Playwright")


# Interactive mode (REPL)
# Blocking REPL, as in CLI:

from playwright.sync_api import sync_playwright


playwright = sync_playwright().start()

# Use playwright.chromium, playwright.firefox or playwright.webkit
# Pass headless=False to see the browser UI
browser = playwright.chromium.launch()
page = browser.new_page()
page.goto("http://whatsmyuseragent.org/")
page.screenshot(path="example.png")
browser.close()
playwright.stop()


# Async REPL such as Jupyter Notebook:

from playwright.async_api import async_playwright


playwright = await async_playwright().start()
browser = await playwright.chromium.launch()
page = await browser.new_page()
await page.goto("http://whatsmyuseragent.org/")
await page.screenshot(path="example.png")
await browser.close()
await playwright.stop()


#  Examples:

# Mobile and geolocation
# This snippet emulates Mobile Safari on a device at a given geolocation, navigates to maps.google.com, performs action and takes a screenshot.
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    iphone_11 = p.devices["iPhone 11 Pro"]
    browser = p.webkit.launch(headless=False)
    context = browser.new_context(
        **iphone_11,
        locale="en-US",
        geolocation={"longitude": 12.492507, "latitude": 41.889938 },
        permissions=["geolocation"]
    )
    page = context.new_page()
    page.goto("https://maps.google.com")
    page.click("text=Your location")
    page.screenshot(path="colosseum-iphone.png")
    browser.close()

    
