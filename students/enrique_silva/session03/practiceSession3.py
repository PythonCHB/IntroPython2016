#!/usr/local/bin/python

students=['jenna','nick','paul','danielle','justin']
print(students)
print()
new_students=input('What new students would you like to add? ')
students.append(new_students)
print(students[-1:])
print()
students= ['John Smith','Mary Miller'] + students
print (students)

del students[-1:]
print(students)
print()
del_students=input('What student do you want to delete? ')
print()

if del_students in students:
	students.remove(del_students)
	print (del_students, 'has been deleted')
	print()
else:
	print (del_students,'cannot be deleted because they are not part of the class')
	print()
print ('This is the current list of students: ', students)

print()

for person in students:
	print('Hello', person, 'how are you?')

file=open('alice.txt','r')
text =file.readlines()
file.close()

for line in text:
	print (line)