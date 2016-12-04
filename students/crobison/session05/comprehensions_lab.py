#!/usr/bin/env python3

# Charles Robison
# 2016.10.15
# List Lab

food_prefs = {"name": "Chris",
            "city": "Seattle",
            "cake": "chocolate",
            "fruit": "mango",
            "salad": "greek",
            "pasta": "lasagna"}

# 1. Print the dict by passing it to a string format method, so 
# that you get something like:

# “Chris is from Seattle, and he likes chocolate cake, mango fruit,
# greek salad, and lasagna pasta”
print("{name} is from {city}, and he likes {cake} cake, {fruit} fruit, "
    "{salad} salad, and {pasta} pasta".format(**food_prefs))

# 2. Using a list comprehension, build a dictionary of numbers from zero to
# fifteen and the hexadecimal equivalent (string is fine). (the hex() function
# gives you the hexidecimal representation of a number.)
number_dict = dict([(i, hex(i)) for i in range(16)])
print(number_dict)

# 3. Do the previous entirely with a dict comprehension – should be a one-liner
number_dict = ({i: hex(i) for i in range(16)})
print(number_dict)

# 4. Using the dictionary from item 1: Make a dictionary using the same keys
# but with the number of ‘a’s in each value. You can do this either by editing
# the dict in place, or making a new one. If you edit in place, make a copy
# first!
food_a_dict = ({key: val.count('a') for key, val in food_prefs.items()})
print(food_a_dict)

# 5. Create sets s2, s3 and s4 that contain numbers from zero through twenty,
# divisible 2, 3 and 4.

# Do this with one set comprehension for each set.
s2 = {i for i in range(21) if i % 2 == 0}
print(s2)
s3 = {i for i in range(21) if i % 3 == 0}
print(s3)
s4 = {i for i in range(21) if i % 4 == 0}
print(s4)

# What if you had a lot more than 3? – Don’t Repeat Yourself (DRY).
# create a sequence that holds all the divisors you might want – could be 2,3,4,
# or could be any other arbitrary divisors.
# loop through that sequence to build the sets up – so no repeated code. you
# will end up with a list of sets – one set for each divisor in your sequence.
# The idea here is that when you see three (Or more!) lines of code that are
# almost identical, then you you want to find a way to generalize that code and
# have it act on a set of inputs, so the actual code is only written once.
n = 7
divisors = range(2, n + 1)
sets = [set() for i in divisors]
for i, st in zip(divisors, sets):
    [st.add(j) for j in range(21) if not j % i]

print("\nHere are all the sets:\n", sets)

# Extra credit: do it all as a one-liner by nesting a set comprehension inside
# a list comprehension. (OK, that may be getting carried away!)
sets = [{i for i in range(21) if not i % j} for j in range(2, n +1)]
print("\nHere are all the sets from the one liner:\n", sets)

















