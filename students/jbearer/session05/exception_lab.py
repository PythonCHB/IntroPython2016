#!/usr/bin/env/python3
"""
LAB: Exceptions
October 27, 2016
"""

def wrapper():
    
    try:
        userInput = input('Enter ^C or ^D: ')
    except (KeyboardInterrupt, EOFError) as the_error:
        return None
    return userInput

print(wrapper())

