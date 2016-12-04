#!/usr/bin/env python3

# Comprehensions Lab

'''
Note: this is a bit of a “backwards” exercise – we show you code, you figure out what it does.

As a result, not much to submit – don’t worry about it – you’ll have a chance to use these in other exercises.
'''

# === List comprehensions

feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']

comprehension = [delicacy.capitalize() for delicacy in feast] # list of strings

comprehension[0] # 'Lambs'

comprehension[2] # 'Orangutans'

# === Filtering lists with list comprehensions

feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals',
            'fruit bats']

comp = [delicacy for delicacy in feast if len(delicacy) > 6]

len(feast) # 5

len(comp) # 3

# === Unpacking tuples in list comprehensions

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

comprehension = [ skit * number for number, skit in list_of_tuples ]

comprehension[0] # n * string = string repeated; 'lumberjack'

len(comprehension[2]) # 4 * 4 = 16 ('spamspamspamspam')

# === Double list comprehensions

eggs = ['poached egg', 'fried egg']

meats = ['lite spam', 'ham spam', 'fried spam']

comprehension = \
[ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]

len(comprehension) # 6 (0 - 5)

comprehension[0] # 'poached egg and lite spam'
comprehension[1] # 'poached egg and ham spam'
comprehension[5] # 'fried egg and fried spam'

# === Set comprehensions

comprehension = { x for x in 'aabbbcccc'} # {} defines dictionary, or set

comprehension # {'a', 'b', 'c'} type = set

# === Dictionary comprehensions

dict_of_weapons = {'first': 'fear',
    'second': 'surprise',
    'third': 'ruthless efficiency',
    'forth': 'fanatical devotion',
    'fifth': None}

dict_comprehension = \
{ k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

'first' in dict_comprehension # Guess: None Actual: False

'FIRST' in dict_comprehension # True

len(dict_of_weapons) # 5

len(dict_comprehension) # 4

# === Count Even Numbers

'''
This is from CodingBat “count_evens” (http://codingbat.com/prob/p189616)

Using a list comprehension, return the number of even integers in the given array.

Note: the % “mod” operator computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) == 3

count_evens([2, 2, 0]) == 3

count_evens([1, 3, 5]) == 0

def count_evens(nums):
   one_line_comprehension_here
'''

def count_evens(list_of_numbers):
    result = len([evens for evens in list_of_numbers if evens % 2 == 0])
    return result

# Breaking down what's happening in the list comprehension:

# list_of_numbers = [2, 1, 2, 3, 4]
# result = []
# for evens in list_of_numbers:
#     if evens % 2 == 0:
#         result.append(evens)
# result = len(result)
# print(result, 'type = ', type(result))

print('\ncount_evens([2, 1, 2, 3, 4])')
print(count_evens([2, 1, 2, 3, 4])) # 3

print('\ncount_evens([2, 2, 0])')
print(count_evens([2, 2, 0])) # 3

print('\ncount_evens([1, 3, 5])')
print(count_evens([1, 3, 5])) # 0

'''
1. Print the dict by passing it to a string format method, so that you get 
something like:

“Chris is from Seattle, and he likes chocolate cake, mango fruit,
greek salad, and lasagna pasta”

'''

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

food_prefs_string = '''\
{} is from {}, and he likes {} cake, {} fruit, {} salad, and {} pasta
'''

print('\n', food_prefs_string.format(
    food_prefs['name'], 
    food_prefs['city'],
    food_prefs['cake'],
    food_prefs['fruit'],
    food_prefs['salad'],
    food_prefs['pasta'],
    ))

'''

2. Using a list comprehension, build a dictionary of numbers from zero to 
fifteen and the hexadecimal equivalent (string is fine). (the hex() function 
gives you the hexidecimal representation of a number.)

Do the previous entirely with a dict comprehension – should be a one-liner

'''

hex_dictionary = { i: hex(i) for i in range(16) }
print('\nhex_dictionary:\n',hex_dictionary)

# hex_dictionary = {}
# for i in range(16):
#     hex_dictionary[i] = hex(i) # returns string
# print(hex_dictionary)

'''

4. Using the dictionary from item 1: Make a dictionary using the same keys but 
with the number of ‘a’s in each value. You can do this either by editing the 
dict in place, or making a new one. If you edit in place, make a copy first!

'''

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

food_a_dictionary = {entry: food_prefs[entry].count('a') for entry in food_prefs}
print('\nfood_a_dictionary:\n', food_a_dictionary)

# food_a_dictionary = {}
# for entry in food_prefs:
#     food_a_dictionary[entry] = food_prefs[entry].count('a')
# print(food_a_dictionary)

'''
5. Create sets s2, s3 and s4 that contain numbers from zero through twenty, 
divisible 2, 3 and 4.

Do this with one set comprehension for each set.
What if you had a lot more than 3? – Don’t Repeat Yourself (DRY)
create a sequence that holds all three sets
loop through that sequence to build the sets up – so no repeated code.
Extra credit: do it all as a one-liner by nesting a set comprehension inside a 
list comprehension. (OK, that may be getting carried away!)
'''

# s = "a not very long string"
# vowels = set('aeiou')
# { l for l in s if l in vowels }
# 
# s2 = set(range(0, 21, 2))
# s3 = set(range(0, 21, 3))
# s4 = set(range(0, 21, 4))

# Create divisible sets as separate comprehensions
set_2 = {i for i in range(21) if i % 2 == 0}
set_3 = {i for i in range(21) if i % 3 == 0}
set_4 = {i for i in range(21) if i % 4 == 0}
print('\nset_2:\n', set_2)
print('\nset_3:\n', set_3)
print('\nset_4:\n', set_4)

# Create a list of divisible sets
list_of_sets = list()
for j in range(2,10):
    list_of_sets.append({i for i in range(21) if i % j == 0})
print('\nlist_of_sets:\n', list_of_sets)

# Create a dictionary of divisible sets
dictionary_of_sets = {}
for j in range(2,10):
    dictionary_of_sets[j] = {i for i in range(21) if i % j == 0}
print('\ndictionary_of_sets:\n', dictionary_of_sets)

# Create a list of divisible sets as a single-line comprehension
list_of_sets = [{i for i in range(21)if i % j == 0} for j in range(2,10)]
print('\nlist_of_sets\n', list_of_sets)

# Create a dictionary of divisible sets as a single-line comprehension
dictionary_of_sets = {j: {i for i in range(21) if i % j == 0} for j in range(2,10)}
print('\ndictionary_of_sets:\n', dictionary_of_sets)

if __name__ == '__main__':
    print('\n=== MAIN ===\n')

'''
=== SAMPLE ===

In [77]: run comprehensions_lab.py

count_evens([2, 1, 2, 3, 4])
3

count_evens([2, 2, 0])
3

count_evens([1, 3, 5])
0

 Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta


hex_dictionary:
 {0: '0x0', 1: '0x1', 2: '0x2', 3: '0x3', 4: '0x4', 5: '0x5', 6: '0x6', 7: '0x7', 8: '0x8', 9: '0x9', 10: '0xa', 11: '0xb', 12: '0xc', 13: '0xd', 14: '0xe', 15: '0xf'}

food_a_dictionary:
 {'pasta': 3, 'cake': 1, 'city': 1, 'fruit': 1, 'name': 0, 'salad': 0}

set_2:
 {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

set_3:
 {0, 3, 6, 9, 12, 15, 18}

set_4:
 {0, 4, 8, 12, 16, 20}

list_of_sets:
 [{0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}, {0, 3, 6, 9, 12, 15, 18}, {0, 4, 8, 12, 16, 20}, {0, 10, 20, 5, 15}, {0, 18, 12, 6}, {0, 14, 7}, {0, 8, 16}, {0, 9, 18}]

dictionary_of_sets:
 {2: {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}, 3: {0, 3, 6, 9, 12, 15, 18}, 4: {0, 4, 8, 12, 16, 20}, 5: {0, 10, 20, 5, 15}, 6: {0, 18, 12, 6}, 7: {0, 14, 7}, 8: {0, 8, 16}, 9: {0, 9, 18}}

list_of_sets
 [{0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}, {0, 3, 6, 9, 12, 15, 18}, {0, 4, 8, 12, 16, 20}, {0, 10, 20, 5, 15}, {0, 18, 12, 6}, {0, 14, 7}, {0, 8, 16}, {0, 9, 18}]

dictionary_of_sets:
 {2: {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}, 3: {0, 3, 6, 9, 12, 15, 18}, 4: {0, 4, 8, 12, 16, 20}, 5: {0, 10, 20, 5, 15}, 6: {0, 18, 12, 6}, 7: {0, 14, 7}, 8: {0, 8, 16}, 9: {0, 9, 18}}

=== MAIN ===

'''