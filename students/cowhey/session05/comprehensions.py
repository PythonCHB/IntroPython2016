feast = ['lambs',
         'sloths',
         'orangutans',
         'breakfast cereals',
         'fruit bats']

comprehension = [delicacy.capitalize() for delicacy in feast]


# prints "Lambs"
print(comprehension[0])

# prints "Orangutans"
print(comprehension[2])

comp = [delicacy for delicacy in feast if len(delicacy) > 6]

# prints 5
print(len(feast))

# prints 3
print(len(comp))

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

comprehension = [skit * number for number, skit in list_of_tuples]

# prints "lumberjack"
print(comprehension[0])

# prints "spamspamspamspam"
print(len(comprehension[2]))

eggs = ['poached egg', 'fried egg']

meats = ['lite spam', 'ham spam', 'fried spam']

comprehension = ['{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]

# prints 6
print(len(comprehension))

# prints "poached egg and lite spam"
print(comprehension[0])

comprehension = {x for x in 'aabbbcccc'}

# prints {'a', 'b', 'c'}
print(comprehension)

dict_of_weapons = {'first': 'fear',
                   'second': 'surprise',
                   'third': 'ruthless efficiency',
                   'forth': 'fanatical devotion',
                   'fifth': None}

dict_comprehension = {k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

# prints False
print('first' in dict_comprehension)

# prints True
print('FIRST' in dict_comprehension)

# prints 5
print(len(dict_of_weapons))

# prints 4
print(len(dict_comprehension))


def count_evens(arr):
    return len([x for x in arr if x % 2 == 0])


food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

# prints “Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta”
print("{} is from {}, and he likes {} cake, {} fruit, {} salad, and {} pasta."
      .format(food_prefs["name"], food_prefs["city"], food_prefs["cake"], food_prefs["fruit"], food_prefs["salad"], food_prefs["pasta"]))

hexed_dictionary = {x:hex(x) for x in range(16)}
print(hexed_dictionary)

a_food_prefs = {k:"a"*len(v) for k, v in food_prefs.items()}
print(a_food_prefs)

s2 = set([x for x in range(21) if x % 2 == 0])
print(s2)

s3 = set([x for x in range(21) if x % 3 == 0])
print(s3)

s4 = set([x for x in range(21) if x % 4 == 0])
print(s4)

sets = [s2, s3, s4]

nested_set = [set([x for x in range(21) if x % n == 0]) for n in range(2, 5)]
print(nested_set)
