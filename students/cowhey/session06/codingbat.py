#!/usr/bin/env python

"""
Examples from: http://codingbat.com

Put here so we can write unit tests for them ourselves
"""

# Python > Warmup-1 > sleep_in

# The parameter weekday is True if it is a weekday, and the parameter
# vacation is True if we are on vacation.
#
# We sleep in if it is not a weekday or we're on vacation.
# Return True if we sleep in.


def sleep_in(weekday, vacation):
    return not weekday or vacation


# We have two monkeys, a and b, and the parameters a_smile and b_smile
# indicate if each is smiling.

# We are in trouble if they are both smiling or if neither of them is
# smiling.

# Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
    return (a_smile and b_smile) or (not a_smile and not b_smile)


# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20.
# Return True if we are in trouble.
def parrot_trouble(hour, talking):
    return (hour < 7 or hour >= 20) and talking


# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.
def not_string(str):
    if str[:3] == "not":
        return str
    else:
        return "not " + str
