
def safe_input():
    try:
        input_response = input('safe input==>').split()
    except (EOFError, KeyboardInterrupt) as the_error:
        print('None')
safe_input()


#def input():
#    try:
#        input_response = input('input ==>').split() 
#    except (EOFError, KeyboardInterrupt) as the_error:
#        raise the_error
#input()


# EOFError, an end-of-file condition (EOF) without reading any data.
# IOError: an I/O-related reason
# KeyboardInterrupt, when the user hits the interrupt key (normally Control-C or Delete).

 
