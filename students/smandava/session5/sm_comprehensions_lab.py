"""Oct 29, 2016 Comprehensions Lab."""

# List Comprehensions.
feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bars']
comprehension = [delicacy.capitalize() for delicacy in feast]
print("Comprehension 0: Lambs:", comprehension[0])
print("Comprehension 2: Orangutans:", comprehension[2])

# Filtering lists with list comprehensions.
comp = [delicacy for delicacy in feast if len(delicacy) > 6]
print("Length of feast:5:", len(feast))
print("Length of comp:3:", len(comp))
print("Comp:", comp)

# Unpacking tuples in list comprehensions
list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
list_comprehension = [skit * number for number, skit in list_of_tuples]
print("list_comprehension:", list_comprehension)
print("list_comprehension 0:", list_comprehension[0])
print("list_comprehension[2] length: 4 or 16: ", len(list_comprehension[2]))

# Double list comprehensions
eggs = ['poached egg', 'fried egg']
meats = ['lite spam', 'ham spam', 'fried spam']
d_list_comprehension = ['{0} and {1}'.format(egg, meat) for egg in eggs
                        for meat in meats]
print("d_list_comprehension:", d_list_comprehension)
print("Length of d_list_comprehension:6:", len(d_list_comprehension))
print("d_list_comprehension[0]:", d_list_comprehension[0])

# Set Comprehensions
set_comprehension = {x for x in 'aabbcccc'}
print("set_comprehension:a,b,c:", set_comprehension)

# Dictionary comprehension
dict_of_weapons = {'first': 'fear', 'second': 'surprise',
                   'third': 'ruthless efficiency',
                   'forth': 'fanatical devotion', 'fifth': None}
dict_comprehension = {k.upper(): weapon for k, weapon in
                      dict_of_weapons.items() if weapon}

print("first in dict_comprehension:", 'first' in dict_comprehension)
print(("FIRST in dict_comprehension:", 'FIRST' in dict_comprehension))
print("Length of dict_of_weapons:5:", len(dict_of_weapons))
print("Length of dict_comprehension:4:", len(dict_comprehension))

# Number of even integers in the given array
print("Number of even integers in the given array.")
# count_evens([2, 1, 2, 3, 4])
# count_evens2([2, 2, 0])
# count_event3([1,3,5])


def count_evens(nums):
    """Return the even integers count."""
    even_count = 0
    for num in nums:
        if num % 2 == 0:
            even_count += 1
    print("Number of even numbers:", even_count)

numbers = ([2, 1, 2, 3, 4])
even_comprehension = [num for num in numbers if num % 2 == 0]
print("even_comprehension count:", len(even_comprehension))


food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

print('{} is from {}, and he likes {} cake, {} fruit, {} salad, {} pasta'.
      format(food_prefs['name'], food_prefs['city'], food_prefs['cake'],
             food_prefs['fruit'], food_prefs['salad'], food_prefs['pasta']))

# 0 to 15 hex representation using list and dict comprehension
numbers_list_comprehension = [hex(hexnum) for hexnum in range(16)]
print("Hex number from zero to fifteen:", numbers_list_comprehension)


numbers_dict_comprehension = {hexnum: hex(hexnum) for hexnum in range(16)}
print("Items from zero to fifteen:", numbers_dict_comprehension)

# Food prefs dictionary with the number of of 'a's as value.
food_prefs_copy = food_prefs.copy()
food_prefs_dict = {key: food_prefs_copy[key].count('a') for key in
                   food_prefs_copy.keys()}
print("key: count of a:", food_prefs_dict)

# s2 divisible by 2, s3 divisible by 3, s4 divisible by 4.
s2_set_comp = {num for num in range(21) if num % 2 == 0}
s3_set_comp = {num for num in range(21) if num % 3 == 0}
s4_set_comp = {num for num in range(21) if num % 4 == 0}

divisors_set = {2, 3, 4, 5, 6}
combined_divisors_set_comp = {num for num in range(21) for divisor in
                              divisors_set if num % divisor == 0}
individual_divisors_set_comp = [[num for num in range(21)
                                 if num % divisor == 0]
                                for divisor in divisors_set]

print("combined_divisors_set_com:", combined_divisors_set_comp)
print("individual_divisors_set_comp:", individual_divisors_set_comp)
