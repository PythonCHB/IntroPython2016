#!/Users/jhefner/python_dev/uw_python/bin/python

# Learning Exceptions
# Just a little bit for the basics.

# Exceptions Lab
# Improving input

# The input() function can generate two exceptions: EOFError or KeyboardInterrupt on end-of-file(EOF) or canceled input.

# Create a wrapper function, perhaps safe_input() that returns None rather rather than raising these exceptions, when the user enters ^C for Keyboard Interrupt, or ^D (^Z on Windows) for End Of File.

# Update your mailroom program to use exceptions (and IBAFP) to handle malformed numeric input

def safe_input():
    try:
        i = input("\n>>> ")
    except (KeyboardInterrupt, EOFError) as error:
        print(error)
        return None
    return i

def main():
    safe_input()

if __name__ == '__main__':
    main()