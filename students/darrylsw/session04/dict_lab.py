#!/usr/bin/env python3

d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

print (d)

popped = d.pop('cake')
#popped = d.popitem()

print (d)

print (popped)

d['fruit'] = 'mango'

print (d)

print (d.keys())

print ("\nKeys")
for key in d.keys():
	print (key)

print ("\nValues")
for value in d.values():
	print (value)
