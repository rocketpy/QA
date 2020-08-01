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

  
from behave import given, when, then


@given(u'I load the website')
def step_impl_load_website(context):
  print('I load the website')
  
@when(u'I go to "{page}" page')
def step_impl_goto_page(context, page):
  print('I go to {} page'.format(page))
  
@then(u'I see this component "{component}"')
  def step_impl_verify_component(context, component):
  print('I see this component "{}"'.format(component))
  
