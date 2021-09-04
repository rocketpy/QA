#  Assertpy - Simple assertion library for unit testing in python with a fluent API

# PyPi: https://pypi.org/project/assertpy/
# Github: https://github.com/assertpy/assertpy
# Docs: https://assertpy.github.io/docs.html

# pip install assertpy


# Examples
from assertpy import assert_warn


assert_warn('foo').is_length(4)
assert_warn('foo').is_empty()
assert_warn('foo').is_false()
assert_warn('foo').is_digit()
assert_warn('123').is_alpha()


from assertpy import assert_that

def test_something():
    assert_that(1 + 2).is_equal_to(3)
    assert_that('foobar').is_length(6).starts_with('foo').ends_with('bar')
    assert_that(['a', 'b', 'c']).contains('a').does_not_contain('x')
    
