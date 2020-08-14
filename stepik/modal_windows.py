

# call modal window by JS
alert('Hello!');

# press button 'Ok' on modal window , named ALERT
alert = browser.switch_to.alert
alert.accept()

# Get a Text from modal window:
alert = browser.switch_to.alert
alert_text = alert.text

# Modal window with 'Ok' and 'Cancel' , named CONFIRM
confirm = browser.switch_to.alert
confirm.accept()  # press Ok
# and
confirm.dismiss()  # press 'Cancel'

# Modal window with input field, named PROMPT
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
