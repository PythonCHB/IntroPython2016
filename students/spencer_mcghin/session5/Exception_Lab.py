def safe_input(input_string=""):
    try:
        n = input(input_string)
        return n
    except (KeyboardInterrupt, EOFError):
        return None


if __name__ == "__main__":
    n = safe_input("Provide a string: ")
    if n is None:
        print("Program terminated by user.")
    else:
        print("User responded with:", n)







