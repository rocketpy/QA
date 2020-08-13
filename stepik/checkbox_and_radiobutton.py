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

# using method get_attribute()
"""
<input class="check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>

people_radio = browser.find_element_by_id("peopleRule")
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"
"""
#  assert people_checked == "true", "People radio is not selected by default"

"""
robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None
"""

# disabled attribute for button "Submit"
# <button type="submit" class="btn btn-default" disabled>Submit</button>

