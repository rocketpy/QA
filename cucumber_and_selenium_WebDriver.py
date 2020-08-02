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
  
  
from behave import given, when, then


@then(u'Dashboard Status shows correct values for row "{row}"')
def step_impl_dashboard_status(context, row):
  print('Dashboard Status for row {}'.format(row))
  
@then(u'Clicking on Status Refresh should refresh status component')
def step_impl_status_refresh(context):
  print('Status Refresh button')
  
@then(u'Dashboard Battery shows Battery or AC Power with correct icon.')
def step_impl_battery_status(context):
  print('Dashboard battery status')
