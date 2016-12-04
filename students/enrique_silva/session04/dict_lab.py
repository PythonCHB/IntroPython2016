#the following lab works with dictionaries and sets

d={'name':'Chris', 'city':'Seattle','cake':'Chocolate'}

print(d)
print()

#delete cake from dictionary

del d['cake']

print(d)
print()

#add mango as a fruit entry

d['fruit']='Mango'

print(d)
print()

#display dict keys

for key in d:
	print (key, end=' ')


print()
#display whether cake is a key in dictionary

if 'cake' in d:
	print('True')

print()
#display whether Mango is in dictionary

if 'Mango'  in d.values():
	print('True')


# function to find number of ts in dictionary values, and substifitute these as new values


d_copy={}

for key, value in d.items():
	d_copy[key]=value.count('t')
print(d_copy)
print()

d.update(d_copy)
print(d)


#set portion of the lab. Create 3 sets and add values to each depeding on if they are a multiple of x
s2=set()
s3=set()
s4=set()

for i in range(21):
	if i % 2 == 0:
		s2.add(i)
	if i % 3 == 0:
		s3.add(i)
	if i % 4 == 0:
		s4.add(i)

print (s2, s3, s4)

#determine if s3 is subset of s2

print(s3.issubset(s2))

#determine if s4 is subset of s2

print(s4.issubset(s2))

#create a set with the letter in Python and add i to the set

new_set=set('Python')

print(new_set)

new_set.add('i')

print (new_set)
print()

#create a frozen set
new_frozen=frozenset(('marathon'))

#display the union and intersection of the two sets
print('union: ', new_set.union(new_frozen))

print()

print('intersection: ', new_set.intersection(new_frozen))
















