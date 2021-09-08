# Webbot - Web Browser automation and testing library for python with more features and simpler api than selenium

# PyPi: https://pypi.org/project/webbot/
# Github: https://github.com/nateshmbhat/webbot

# pip install webbot

from webbot import Browser


web = Browser()
web.go_to('google.com')
web.type('hello its me')  # or web.press(web.Key.SHIFT + 'hello its me')
web.press(web.Key.ENTER)
web.go_back()
web.click('Sign in')
web.type('mymail@gmail.com' , into='Email')
web.click('NEXT' , tag='span')
web.type('mypassword' , into='Password' , id='passwordFieldId')
web.click('NEXT' , tag='span') # you are logged in . woohoooo
 
  
# If multiple buttons with similar properties are to be clicked at once
web = Browser()
web.go_to('siteurl.com')
web.click('buttontext' , multiple = True)


# If there are multiple elements and you want to perform action on one of them

web = Browser()
web.go_to('siteurl.com')
# types the text into the 3rd input element when there are multiple input elements with form-input class
web.type('im robo typing' , number = 3 , classname="form-input" )
web.click('Post')

