#!/usr/bin/env python3

# Test Lab

'''
Pick an example from codingbat:

http://codingbat.com

Do a bit of test-driven development on it:

run something on the web site.
write a few tests using the examples from the site.
then write the function, and fix it ‘till it passes the tests.
Do at least two of these...

$ py.teset test_cigar_party.py

$ py.test codingbat.py

$ pytest (within directory)

'''

from codingbat import count_evens, close_far, end_other

# count_evens

def test_count_evens_a():
    assert count_evens([2, 1, 2, 3, 4]) == 3

def test_count_evens_b():
    assert count_evens([2, 2, 0]) == 3

def test_count_evens_c():
    assert count_evens([1, 3, 5]) == 0

# close_far   

def test_close_far_a():
    assert close_far(1, 2, 10)

def test_close_far_b():
    assert not close_far(1, 2, 3)

def test_close_far_c():
    assert close_far(4, 1, 3)

# end_other

def test_end_other_a():
    assert end_other('Hiabc', 'abc')

def test_end_other_b():
    assert end_other('AbC', 'HiaBc')

def test_end_other_c():
    assert end_other('abc', 'abXabc')