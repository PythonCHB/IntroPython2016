# Coding Bat Count Even Numbers #

# nums = range(0, 88)
#
# def count_evens(nums):
#     evens_count = [number for number in nums if number % 2 == 0]
#     print(len(evens_count))
#
#
# count_evens(nums)


# Dict and Set Comprehension #

food_prefs = {"name": "Spencer",
              "city": "Seattle",
              "cake": "Funfetti",
              "fruit": "Bananas",
              "salad": "Macaroni",
              "pasta": "Spaghetti"}

#
#
# print("{name} is from {city} and he likes {cake} cake. His favorite fruit is {fruit}, his favorite salad is\n"
#       "{salad}, and his favorite pasta is {pasta}.".format(**food_prefs))

# Hexadecimal Function #
#
# def hex_equiv():
#     hex_dict = {number: hex(number) for number in range(16)}
#     print(hex_dict)
#
# hex_equiv()

# A's for Values #

# def a_values():
#     food_a = {k: v.count('a') for (k, v) in food_prefs.items()}
#     print(food_a)
#
#
# a_values()

# Sets Comprehensions #


s_2 = set(i for i in range(21) if i % 2 == 0)
s_3 = set(i for i in range(21) if i % 3 == 0)
s_4 = set(i for i in range(21) if i % 4 == 0)


# Loop function to return multiple rows #

def divisors(n):
    for i in range(n):
        num_sets = set(i for i in range(21) if i % n == 0)
        print(num_sets)

divisors(10)
