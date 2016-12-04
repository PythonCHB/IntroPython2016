def fib(n):
	"""Return the nth value in a fibonacci series"""
	if n==0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib (n-2) + fib (n-1)

print([fib (n) for n in range(20)])


def lucas(n):
	"""Return the nth value in a lucas number series"""
	if n==0:
		return 2
	elif n == 1:
		return 1
	else:
		return lucas (n-2) + lucas (n-1)

print([lucas (n) for n in range(20)])

def sum_series()











