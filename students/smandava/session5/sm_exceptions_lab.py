"""Oct 31, 2016 Exceptions lab."""
try:
    print("Opening missing.txt")
    f = open('missing.txt')
except IOError:
    print("couldn't open missing.txt")
else:
    f.readline()  # only called if there is no exception
finally:
    print("finally.")

try:
    num_in = int(input("Enter a number:"))
except ValueError:
    print("Input must be an integer, try again.")


try:
    print("printing missing.txt")
    f = open('missing.txt')
except (IOError, BufferError, OSError) as missingfile_error:
    print(missingfile_error)
    raise


def divide(a, b):
    """Raise an exception."""
    if b == 0:
        raise ZeroDivisionError("b can not be zero")
    else:
        return a / b


def safe_input():
    """Raise an exception."""
    try:
        user_input = input("Press control + C:")
    except (EOFError, KeyboardInterrupt) as input_error:
        print("No input entered", input_error)
        return None
    return input_error

def main():
    safe_input()

if __name__ == "__main__":
    main()

