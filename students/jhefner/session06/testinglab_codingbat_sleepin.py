#!/Users/jhefner/python_dev/uw_python/bin/python

# Warmup-1 > sleepIn
# http://codingbat.com/prob/p187868


# The parameter weekday is true if it is a weekday, and the parameter vacation is true if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return true if we sleep in.

# sleepIn(false, false) → true
# sleepIn(true, false) → false
# sleepIn(false, true) → true

def sleep_in(weekday, vacation):
  if (weekday == True and vacation == True):
    return True
  elif (weekday == True and vacation == False):
    return False
  elif (weekday == False and vacation == True):
    return True
  elif (weekday == False and vacation == False):
    return True
