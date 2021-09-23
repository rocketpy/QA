#  Golem - Test Automation

# Github: https://github.com/golemhq/golem
# Docs: https://golem-framework.readthedocs.io/en/latest/

# pip install golem-framework

"""
Batteries Included:
    Multi-user web IDE
    Extended classes for WebDriver and WebElement
    More than 200 self documenting Actions
    Webdriver-manager utility
    Built in parallel test support
    Reporting engine
"""

# A test example

# Next is a test that navigates to ‘en.wikipedia.org’, searches an article and validates that the title of the article is correct.
# validate_article_title.py

description = 'Search an article in Wikipedia'

def test_validate_article_title(data):
    navigate('http://en.wikipedia.org/')
    send_keys(('id', 'searchInput'), 'automation')
    click(('id', 'searchButton'))
    verify_element_text(('id', 'firstHeading'), 'Automation')


