# RPA Framework is a collection of open-source libraries and tools for Robotic Process Automation (RPA)

# PyPI: https://pypi.org/project/rpaframework/

# Github: https://www.github.com/robocorp/rpaframework/
# Docs: https://rpaframework.org/


# some example Robot Framework code
*** Settings ***
Documentation     Robot to enter weekly sales data into the RobotSpareBin Industries Intranet.
Library           RPA.Browser.Selenium

*** Variables ***
${URL}=    https://robotsparebinindustries.com/

*** Keywords ***
Open The Intranet Website
    Open Available Browser    ${URL}

*** Keywords ***
Log In
    Input Text    username    maria
    Input Password    password    thoushallnotpass
    Submit Form

*** Tasks ***
Open the intranet site and log in
    Open The Intranet Website
    Log In

