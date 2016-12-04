#!/usr/local/bin/python3

# Author: Darryl Wong (darrylsw@gmail.com)
# Date: 10/23/2016

# Write a format string that will take:
#
#( 2, 123.4567, 10000)
#
#and produce:
#
#'file_002 :   123.46, 1.00e+04'


print ("file_{:03d}: {:.2f} {:.2e}".format(2, 123.4567, 10000))



# Rewrite:
# "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
#
# to take an arbitrary number of values.
#
# Trick: You can pass in a tuple of values to a function with a *:
#
# In [52]: t = (1,2,3)
#
# In [53]: "the 3 numbers are: {:d}, {:d}, {:d}".format(*t)
# Out[53]: 'the 3 numbers are: 1, 2, 3'


# brute force method
# I'll look for more elegant method later
def formatter (formattee):
	length = len(formattee)
	print ("the {} numbers are".format(len(formattee)), end="")
	for i in range (0, len(formattee)-1):	
		print (" {:d},".format(formattee[i]), end="")
	print (" {:d}".format(formattee[length-1]))
	print()

t = (1, 2, 3, 4, 5)
formatter (t)

t = (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
formatter (t)