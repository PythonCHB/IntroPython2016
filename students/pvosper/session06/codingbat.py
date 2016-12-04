#!/usr/bin/env python3

# Coding Bat Samples for Test Lab

'''
Pick an example from codingbat:

http://codingbat.com

Do a bit of test-driven development on it:

run something on the web site.
write a few tests using the examples from the site.
then write the function, and fix it ‘till it passes the tests.
Do at least two of these...
'''

# List 2 > Count Evens
# http://codingbat.com/prob/p189616

'''
Return the number of even ints in the given array. Note: the % "mod" operator 
computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
'''

def count_evens(nums):
    count = len([num for num in nums if num % 2 == 0])
    return count
    
# Logic-2 > close_far
# http://codingbat.com/prob/p160533

'''
Given three ints, a b c, return True if one of b or c is "close" 
(differing from a by at most 1), while the other is "far", differing from 
both other values by 2 or more. Note: abs(num) computes the absolute value of 
a number.

close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
'''

def close_far(num_a, num_b, num_c):
#     if (abs(num_a - num_b) or abs(num_a - num_c) <= 1) and (abs(num_a - num_b) or abs(num_a - num_c) >= 2):
    t1 = abs(num_a - num_b)
    t2 = abs(num_a - num_c)
    t3 = abs(num_b - num_c)
    if t1 <= 1 and t2 >= 2 and t3 >= 2:
        return True
    if t2 <= 1 and t3 >= 2 and t1 >= 2:
        return True
    if t3 <= 1 and t1 >= 2 and t2 >= 2:
        return True
    else:
        return False

# String-2 > end_other 
# http://codingbat.com/prob/p174314

'''
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
'''

def end_other(str_a, str_b):
    if str_a[-3:].lower() == str_b.lower():
        return True
    elif str_b[-3:].lower() == str_a.lower():
        return True
    else:
        return False

if __name__ == '__main__':
    print('\n=== MAIN ===\n')

    print('\nList 2 > Count Evens')
    print('[2, 1, 2, 3, 4]: ', count_evens([2, 1, 2, 3, 4]))
    print('[2, 2, 0]: ', count_evens([2, 2, 0]))
    print('[1, 3, 5]: ', count_evens([1, 3, 5]))
    
    print('\nLogic-2 > close_far')
    print('(1, 2, 10)', close_far(1, 2, 10))
    print('(1, 2, 3)', close_far(1, 2, 3))
    print('(4, 1, 3)', close_far(4, 1, 3))
    
    print('\nString-2 > end_other')
    print("('Hiabc', 'abc')", end_other('Hiabc', 'abc'))
    print("('AbC', 'HiaBc')", end_other('AbC', 'HiaBc'))
    print("('abc', 'abXabc')", end_other('abc', 'abXabc'))
    
    

'''
=== SAMPLE ===

In [1]: run codingbat.py

=== MAIN ===


List 2 > Count Evens
[2, 1, 2, 3, 4]:  3
[2, 2, 0]:  3
[1, 3, 5]:  0

Logic-2 > close_far
(1, 2, 10) True
(1, 2, 3) False
(4, 1, 3) True

String-2 > end_other
('Hiabc', 'abc') True
('AbC', 'HiaBc') True
('abc', 'abXabc') True

'''
