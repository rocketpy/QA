# Qweb - Keyword based test automation for the web.

# Github: https://github.com/qentinelqi/qweb

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
