#!/usr/bin/env python
"""Oct 22, 2016 Dictionary and Set lab."""

d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(d)

d.pop('cake')
print(d)

d['fruit'] = 'Mango'
print(d.keys())

print(d.values())

print('cake' in d)

print('Mango' in d.values())

s2 = set()
s3 = set()
s4 = set()

for i in range(20):
    if (i % 2 == 0):
        s2.add(i)
    if (i % 3 == 0):
        s3.add(i)
    if (i % 4 == 0):
        s4.add(i)


print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

s1 = set('Python')
s1.add('i')

s5 = frozenset('marathon')
print(s1.union(s5))
print(s1.intersection(s5))
