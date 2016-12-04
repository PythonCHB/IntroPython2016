#!/usr/bin/env python

#Given a number n, return True if n is in the range 1..10, 
#inclusive. Unless "outsideMode" is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.

#in1to10(5, False) → True
#in1to10(11, False) → False
#in1to10(11, True) → True

#importing to test version
from in1to10 import in1to10

def test_inRange_True():
	assert in1to10(5, True) == False

def test_inRange_False():
	assert in1to10(5, False) == True

def test_lowBoundry_True():
	assert in1to10(1, True) == True

def test_lowBoundry_True2():
	assert in1to10(2, True) == False

def test_HighBoundry_True():
	assert in1to10(10, True) == True

def test_HighBoundry_True9():
	assert in1to10(9, True) == False

def test_lowBoundry_False():
	assert in1to10(1, False) == True

def test_lowBoundry_False0():
	assert in1to10(0, False) == False

def test_HighBoundry_False():
	assert in1to10(10, False) == True

def test_HighBoundry_False11():
	assert in1to10(11, False) == False

def test_OutRange_True15():
	assert in1to10(15, True) == True

def test_OutRange_TrueLower():
	assert in1to10(-15, True) == True

def test_base3():
	assert in1to10(11, True) == True




