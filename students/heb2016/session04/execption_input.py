
def input_lab():
    try:
        input_response = input('input ==>').split()
    except (EOFError, KeyboardInterrupt) as the_error:
        raise
input_lab()


# EOFError, an end-of-file condition (EOF) without reading any data.
# IOError: an I/O-related reason
# KeyboardInterrupt, when the user hits the interrupt key (normally Control-C or Delete).


