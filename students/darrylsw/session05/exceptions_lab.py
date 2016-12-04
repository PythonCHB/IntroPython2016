#!/usr/local/bin/python3

""" 
The input() function can generate two exceptions: EOFError or KeyboardInterrupt on end-of-file(EOF) or canceled input.
Create a wrapper function, perhaps safe_input() that returns None rather rather than raising these exceptions, when the user 
enters ^C for Keyboard Interrupt, or ^D (^Z on Windows) for End Of File.
Update your mailroom program to use exceptions (and IBAFP) to handle malformed numeric input"""

def safe_input(string):
	try:
		an_input = input (string)
	except EOFError:
		print ("received EOFError")
		return None
	except KeyboardInterrupt:
		print ("received KeyboardInterrupt")
		return None
	else:
		return an_input

def main():
	print (safe_input("Enter input: "))




if __name__ == '__main__':
	main()




