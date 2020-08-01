#  taked from :  https://medium.com/@hmurari/bdd-cucumber-and-selenium-webdriver-based-test-automation-framework-in-python-ae092a7581d3
pip install behave
pip install selenium


@given(u'I load the website')
def step_impl(context):
  raise NotImplementedError(u'STEP: Given I load the website')
  
@when(u'I go to "Dashboard" page')
def step_impl(context):
  raise NotImplementedError(u'STEP: When I go to "Dashboard" page')
  
@then(u'I see this component "Status"')
def step_impl(context):
  raise NotImplementedError(u'STEP: Then I see this component "Status"')
