#!/usr/bin/env python3

'''
Exceptions Lab
Learning Exceptions
Just a little bit for the basics.

Exceptions Lab
Improving input

The input() function can generate two exceptions: EOFError or KeyboardInterrupt
on end-of-file(EOF) or canceled input.
Create a wrapper function, perhaps safe_input() that returns None rather rather
than raising these exceptions, when the user enters ^C for Keyboard Interrupt,
or ^D (^Z on Windows) for End Of File.
Update your mailroom program to use exceptions (and IBAFP) to handle malformed
numeric input

try:
    do_something()
    f = open('missing.txt')
except IOError:
    print("couldn't open missing.txt")
else:
    process(f) # only called if there was no exception
    
Multiple 'exceptions' OK

The finally: clause will always run

Example of no exception handling:
In [3]: response = input('->')
->^C---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-3-f9c05402e592> in <module>()
----> 1 response = input('->')

KeyboardInterrupt: 

'''

def safe_input():
    try:
        response = input('->')
    except EOFError:
        print('\nHandled exception: EOFError')
        return None
    except KeyboardInterrupt:
        print('\nHandled exception: KeyboardInterrupt')
        return None
    else:
        print('\nValid Input')
        return response
    finally:
        print('\nThe finally clause will always run\n')
    
if __name__ == '__main__':
    print('\n=== MAIN ===\n')
    
    print('\nsafe_input() will return None rather than raising exceptions')
    print('\nEnter ^C for Keyboard Interrupt:')
    print(safe_input())
    print('\nEnter ^D (^Z on Windows) for End Of File.')
    print(safe_input())
    print('\nEnter anything.')
    print('\nReturn: ', safe_input())
    # ? When safe_input() returns None, this last print statement doesn't
    #    actually print - so instead of seeing 'Return: None', you just see
    #    'None'.

'''
=== SAMPLE ===

In [13]: run exceptions_lab.py

=== MAIN ===


safe_input() will return None rather than raising exceptions

Enter ^C for Keyboard Interrupt:
->^C
Handled exception: KeyboardInterrupt

The finally clause will always run

None

Enter ^D (^Z on Windows) for End Of File.
->^D
Handled exception: EOFError

The finally clause will always run

None

Enter anything.
->Donor: Bob

Valid Input

The finally clause will always run


Return:  Donor: Bob
'''
