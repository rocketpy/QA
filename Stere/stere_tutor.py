# Stere - A nice way of implementing the Page Object pattern.
# Stere is a library for writing Page Objects, designed to work on top of an existing automation library.

# PyPi: https://pypi.org/project/stere/
# Github: https://github.com/jsfehler/stere
# Docs: https://stere.readthedocs.io/en/latest/

# pip install stere

"""
Design Philosophy
Many implementations of the Page Object model focus on removing the duplication of element locators inside tests.
Stere goes one step further, offering a complete wrapper over the code that drives automation.
The goals of this project are to:
1 - Eliminate implementation code in test functions. Tests should read like a description of behaviour, not Selenium commands.
2 - Reduce the need for hand-written helper methods in Page Objects. Common actions should have universal solutions.
3 - Provide a simple pattern for writing maintainable Page Objects.
No automation abilities are built directly into the project; it completely relies on being hooked into other libraries.
However, implementations using Splinter and Appium are available out of the box.
"""

# As an example, here’s the home page for Wikipedia:
from stere import Page
from stere.areas import Area, RepeatingArea
from stere.fields import Button, Input, Link, Root, Text


class WikipediaHome(Page):
    def __init__(self):
        self.search_form = Area(
            query=Input('id', 'searchInput'),
            submit=Button('xpath', '//*[@id="search-form"]/fieldset/button')
        )

        self.other_projects = RepeatingArea(
            root=Root('xpath', '//*[@class="other-project"]'),
            title=Link('xpath', '//*[@class="other-project-title"]'),
            tagline=Text('xpath', '//*[@class="other-project-tagline"]')
        )

        self.commons = Area(
            root=Root('xpath', '//*[@class="other-project"][1]'),
            title=Link('xpath', '//*[@class="other-project-title"]'),
            tagline=Text('xpath', '//*[@class="other-project-tagline"]')
        )

        self.wikivoyage = Area(
            root=Root('xpath', '//*[@class="other-project"][2]'),
            title=Link('xpath', '//*[@class="other-project-title"]'),
            tagline=Text('xpath', '//*[@class="other-project-tagline"]')
        )


# Using a Page Object in a test can be done like so:
def test_search_wikipedia():
    home = WikipediaHome()
    home.search_form.perform('kittens')

