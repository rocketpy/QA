#  get a current page name (number)
current_window = browser.current_window_handle

# go to window_name:
browser.switch_to.window(window_name)

# name a second opened window
new_window = browser.window_handles[1]

# first window name
first_window = browser.window_handles[0]
