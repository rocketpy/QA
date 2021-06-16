# behave - uses tests written in a natural language style, backed up by Python code.

# Docs: https://behave.readthedocs.io/en/latest/
# Github: https://github.com/behave/behave

# pip install git+https://github.com/behave/behave


# Now make a directory called “features”. In that directory create a file called “tutorial.feature” containing:
"""
Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!
"""


# Make a new directory called “features/steps”. In that directory create a file called “tutorial.py” containing:

from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False

# Run behave:

# % behave
"""
Feature: showing off behave # features/tutorial.feature:1

  Scenario: run a simple test        # features/tutorial.feature:3
    Given we have behave installed   # features/steps/tutorial.py:3
    When we implement a test         # features/steps/tutorial.py:7
    Then behave will test it for us! # features/steps/tutorial.py:11
"""


