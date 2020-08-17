#  install to venv:
# > selenium_env\Scripts\activate.bat 
# (selenium_env) С:\Users\user\environments>  pip install pytest==5.1.1

# to run PyTest flle:  pytest test_abs_project.py


# a simple example , file with name test_abs.py
def test_abs_1():
    assert abs(-42) == 42, "Should be absolute value of a number"  #  return True

def test_abs_2():
    assert abs(-42) == -42, "Should be absolute value of a number"   # return False
    
#  for run tests in cosole:  pytest test_abs.py 

#  and try add this to command:  -v --tb=line

#  we can use any construction: == , != , e.t.c. 
#  and like this:  assert user_is_authorised(), "User is guest"
