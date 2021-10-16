# Qweb - Keyword based test automation for the web.

# Github: https://github.com/qentinelqi/qweb
# Home page: https://qentinel.com/qweb-open-source-automation-library/

# Windows
# pip install QWeb

# Linux/Mac
# python3 -m pip install -U pip
# python3 -m pip install QWeb

# Examples
"""
Library    QWeb     # Import library

*** Test Cases ***
Basic interaction
    OpenBrowser         https://qentinelqi.github.io/shop      chrome   # Open chrome and goto given url
    VerifyText          The animal friendly clothing company            # Assert heading text
    ClickText           Scar the Lion                                   # Click link text
    ClickText           Add to cart                                     # Click *button* with specific text
    DropDown            Size            Large                           # Select value (Large) from dropdown (Size)
"""

"""
# Timeouts and anchors
By default QWeb tries to locate the element 10 seconds (default time can be configured).
Timeout can also be individually given for each keyword as an argument.

When text to be found is not unique, an 'anchor' argument can be given to pinpoint which instance of text we want
to interact with. Anchor can be either another text nearby or index.

ClickText   Sign-in
ClickText   Sign-in     timeout=30

ClickText   Sign-in     anchor=Email
ClickText   Sign-in     index=3

# Other locators
# Non-textual locators can be used with ClickElementand ClickItemkeywords.

ClickElement    xpath\=//button[@class="my_class"]   # xpath
ClickItem       Increment quantity                   # alt text
"""

# Working with tables
"""
UseTable    Firstname

${row}=     GetTableRow     //last                        # returns 5
${row}=     GetTableRow     //last    skip_header=True    # returns 4
...
${row}=     GetTableRow     Jim                           # returns 4
${row}=     GetTableRow     Jim    skip_header=True       # returns 3

${cell_value}=     GetCellText     r1c2                   # Returns "John", first name is column 2.

${cell_value}=     GetCellText     r-1/c2                 # Returns "Tina", -1 points to last row
${cell_value}=     GetCellText     r-2/c2                 # Returns "Jim", -2 points to second last row
"""

