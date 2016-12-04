#!/usr/bin/env/python3
"""
LAB: pytest
November 1, 2016
"""

def monkey_trouble(a_smile, b_smile):
    return a_smile is b_smile

def squirrel_play(temp, is_summer):
    if temp >= 60 and temp <= 100 and is_summer or temp >= 60 and temp <= 90:
        return True
    else:
        return False
