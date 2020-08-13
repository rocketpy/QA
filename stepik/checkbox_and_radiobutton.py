#  <input type="radio" name="language" value="python" checked>
elem = browser.find_element_by_css_selector("[value='python']")
elem.click()

"""
<input type="checkbox">  # we can make choice for many elems 
<input type="radio">  # we can make choice only for one elem 

#  checked
<input type="checkbox" checked>
<input type="radio" checked>

<input type="radio" name="language" value="python" checked>
<input type="radio" name="language" value="selenium">
"""

# using tag <label> , this tag make text a cklickable !!!
option1 = browser.find_element_by_css_selector("[for='python']")
option1.click()

"""
<div>
  <input type="radio" id="python" name="language" checked>
  <label for="python">Python</label>
</div>
"""

