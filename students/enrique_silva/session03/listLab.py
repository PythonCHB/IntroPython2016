#list lab, working with lists.

#create a list of fruits and print the list
fruits=['Apples','Pears','Oranges','Peaches']

print(fruits)
print()

#request input from user to add a fruit to the list
new_fruits=input('What fruits would you like to add to the list? ')

fruits.append(new_fruits)

print(fruits)
print()

#display the fruit based on the number the customer chooses.
number_fruits=int(input('Pick a number: '))

print("You picked #", number_fruits, "which means your fruit is: ", fruits[number_fruits-1])
print()

#add fruits to the list using several different methods.
fruits=['watermelon'] + fruits

print(fruits)
print()

fruits.insert(0,'cantelope')

print(fruits)
print()

#create a loop that iterates on the list and prints out in a new list all
#the fruits tha start with a P
fruits_with_p=[]

for name in fruits:
	if name.startswith('p') or name.startswith('P'):
		fruits_with_p.append(name)

print(fruits_with_p)
print()

#display the list and Remove the last fruit from the list.
print(fruits)
print()

fruits.pop()

print(fruits)
print()

#Ask the user for a fruit to delete and find it and delete it.

delete_fruit=input('What fruit would you like to delete? ')

if delete_fruit in fruits:
	fruits.remove(delete_fruit)
	print(fruits)
else:
	print('Fruit does not exist')












