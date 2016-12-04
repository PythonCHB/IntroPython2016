#!/usr/bin/env python

#Given 3 int values, a b c, return their sum. However, 
#if one of the values is the same as another of the values, 
#it does not count towards the #sum.

#lone_sum(1, 2, 3) → 6
#lone_sum(3, 2, 3) → 2
#lone_sum(3, 3, 3) → 0

#importing to test version
from lone_sum import lone_sum

def test_1():
    assert lone_sum(1, 2, 3) == 6

def test_2():
    assert lone_sum(3, 2, 3) == 2

def test_3():
    assert lone_sum(3, 3, 3) == 0

