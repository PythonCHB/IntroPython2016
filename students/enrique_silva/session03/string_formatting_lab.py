
#Enrique Silva
#String formatiting lab practice

data={'first':2, 'second':123.4567, 'third':10000}

print('The file is file_00{first}, the decimal is {second:.2f}, the scientific notation of the number is {third:.2e}'.format(**data))
print()

print("the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3))
print()

t=(1,2,3)
print("the 3 numbers are: {:d}, {:d}, {:d}".format(*t))
print()

#Dynamically build up a format string, with an arbitraty number of items in a tuple.

number_list=int(input("Enter the number of items you would like in the tuple: " ))
my_list=tuple(range(number_list))

format_list="The {:d} numbers are:  ".format(my_list)

for i in my_list:
    format_list += " , ".join(['{:d}'])


print(format_list)

