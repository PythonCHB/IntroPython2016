"""
Name: Paul Briant
Date: 11/1/16
Class: Introduction to Python
Session05
LAB: Exceptions

Description:
This program creates a wrapper to deal with the two possible exceptions for
the input function.
"""

# -------------------------------Import-----------------------------------------

# -------------------------------Functions--------------------------------------


def safe_input(question):
    """
    Takes in a multiword string and returns None if an exception is thrown.
    """
    try:
        answer = input(question)
        print(answer)
    except KeyboardInterrupt:
        return None
    except EOFError:
        return None

# ==============================================================================


def main():
    """
    Tests output.
    """

    safe_input("What is your name? ")

if __name__ == '__main__':
    main()
