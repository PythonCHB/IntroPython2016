#!/usr/bin/env python3

# Charles Robison
# 2016.11.08
# Exceptions Lab

def none():
    try:
        answer = input('Who will be the next President? ')
        print('Really?  You think ' + answer +"?!")
    except (KeyboardInterrupt) as e:
        return None

none()