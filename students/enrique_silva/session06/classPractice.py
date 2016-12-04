
#handling an exception, class example.

def divide(x,y):
	try:
		return x/y
	except ZeroDivisionError as err:
		print(err)
		raise ###still unsure why this is needed.

result= divide (2,2)

print(result)



