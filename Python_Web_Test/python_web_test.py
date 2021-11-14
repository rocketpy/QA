#  Selene + Pytest tests project template

# Github: https://github.com/yashaka/python-web-test

# Installation

   # pyenv + python: https://github.com/pyenv/pyenv
   # poetry: https://poetry.eustace.io/docs/#installation
   # allure: https://docs.qameta.io/allure/#_installing_a_commandline
  
# Clone template with: git clone

# in your favourite terminal:
# cd $YOUR_PROJECT_FOLDER_PATH
# poetry install
# poetry shell

# run your tests via:
# pytest tests/

# example of reported test case with PageObejcts

def test_ecosia():
    ecosia.open()

    ecosia.search('selene python')
    ecosia.results\
        .should_have_size_at_least(5)\
        .should_have_text(0, 'User-oriented Web UI browser tests')

    ecosia.results.follow_link(0)
    github.should_be_on('yashaka/selene')

"""
reporting steps with automatic rendering of

    underscores to spaces
    inline params
    context of step-function (object, class or module)
    actions on raw selene elements

last screenshot and page-source are attached to test body on failure

use allure webserver to see reports with webui:

# allure serve reports

"""

