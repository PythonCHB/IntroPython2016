#!/usr/bin/env python

#Given a number n, return True if n is in the range 1..10, inclusive. 
#Unless "outsideMode" is True, in which case return True if the number is #less or equal to 1, or greater or equal to 10.

#in1to10(5, False) → True
#in1to10(11, False) → False
#in1to10(11, True) → True

def in1to10(n, outsideMode):
	#if outsideMode == False and n >=1 and n <=10:
	#	return True
	#if outsideMode == True and (n <=1 or n >=10):
	#	return True
	#return False

	#refactored version
	return outsideMode and (n <=1 or n >=10) or not outsideMode and (n >=1 and n <=10)