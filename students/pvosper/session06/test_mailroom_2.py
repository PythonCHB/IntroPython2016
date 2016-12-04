#!/usr/bin/env python3

# Test Mailroom_2

'''
Write a complete set of unit tests for your mailroom program.

You will likely find that it is really hard to test without refactoring.

This is Good!

If code is hard to test – it probably should be refactored.

$ py.test test_mailroom_2.py 

'''

from mailroom_2 import donor_name_length, donor_average, donor_total, find_donor

# Return length of longest name for print formatting
# donor_name_length(donor_list.keys())

def test_donor_name_length_list():
    assert donor_name_length(['abcd', 'efghij', 'klm', 'nopqrstuv']) == 9

def test_donor_name_length_dictionary():
    test_dictionary = {
        "1234" : [1, 2, 3],
        "bob" : [1, 2, 3],
        "ingt" : [1, 2, 3],
        "nghbdysbgldjsufgbgsvs" : [4],
        "fnnf" : [5, 6, 7],
        "mnfsdkhf" : [8, 9]
        }
    assert donor_name_length(test_dictionary.keys()) == 21
    
# Return average donation from list
# donor_average(donor_list[key])

def test_donor_average_a():
    assert donor_average([50, 100]) == 75

def test_donor_average_b():
    test_dictionary = {
        "1234" : [1, 2, 3],
        "bob" : [1, 2, 3],
        "ingt" : [1, 2, 3],
        "nghbdysbgldjsufgbgsvs" : [4],
        "fnnf" : [5, 6, 7],
        "mnfsdkhf" : [8, 9]
        }
    assert donor_average(test_dictionary['bob']) == 2

# Return total of donations from list
# donor_total(donor_list[key])

def test_donor_total():
    assert donor_total([50, 100]) == 150

def test_donor_total():
    test_dictionary = {
        "1234" : [1, 2, 3],
        "bob" : [1, 2, 3],
        "ingt" : [1, 2, 3],
        "nghbdysbgldjsufgbgsvs" : [4],
        "fnnf" : [5, 6, 7],
        "mnfsdkhf" : [8, 9]
        }
    assert donor_total(test_dictionary['mnfsdkhf']) == 17

# Return the full name of a donor from list given a partial string    
# find_donor(donor_list.keys())

def test_find_donor_a():
    assert find_donor('foo', ['foobar', 'gahbar']) == 'foobar'
find_donor('zzz', ['foobar', 'gahbar'])

def test_find_donor_b():
    assert find_donor('zzz', ['foobar', 'gahbar']) == None

def test_find_donor_c():
    test_dictionary = {
        "1234" : [1, 2, 3],
        "bob" : [1, 2, 3],
        "ingt" : [1, 2, 3],
        "nghbdysbgldjsufgbgsvs" : [4],
        "fnnf" : [5, 6, 7],
        "mnfsdkhf" : [8, 9]
        }
    assert find_donor('ysbgl', test_dictionary.keys()) == 'nghbdysbgldjsufgbgsvs'
