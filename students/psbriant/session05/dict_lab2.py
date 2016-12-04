# !/usr/bin/env python3
"""
Name: Paul Briant
Date: 11/1/16
Class: Introduction to Python
Session05
LAB: Dictionaries

Description:
This module takes the dictionary lab from Session04 and incorporates
comprehensions.
"""

# -------------------------------Functions--------------------------------------


def part1(dict1):
    """
    Explores adding, deleting, displaying and verifying values and keys in
    dictionaries.
    """
    print(dict1)
    del dict1["cake"]
    print(dict1)
    dict1["fruit"] = "Mango"
    print(dict1.keys())
    print(dict1.values())
    print("cake" in dict1)
    print("Mango" in dict1.values())


def part2(dict1):
    """
    Takes in a dictionary and returns the count of the letter 't' in each
    value.
    """
    # Creat a new dictionary with identical values to dict1
    new_dict = dict1

    # Iterate through keys
    for key in dict1:
        count = 0
        # Iterate through values
        for char in dict1[key]:
            if char == 't':
                count += 1
        # Add count to each key
        new_dict[key] = count
    return new_dict


def part3():
    """
    Creates three sets, displays them and determines which are subsets.
    """
    # Ints divisible by 2
    s2 = set([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
    # Ints divisible by 3
    s3 = set([3, 6, 9, 12, 15, 18])
    # Ints divisible by 4
    s4 = set([4, 8, 12, 16, 20])
    print(s2, s3, s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))


def part4():
    """
    Creates a set and frozenset and displays the intersection and union of
    both.
    """
    python_set = set(['P', 'y', 't', 'h', 'o', 'n'])
    python_set.add('i')
    fs = frozenset(['m', 'a', 'r', 'a', 't', 'h', 'o', 'n'])
    print(python_set.union(fs), python_set.intersection(fs))


def display_dict(info_dict):
    """
    Takes in the info_dict and displays it using string formatting and an
    advanced function call.
    """
    print("{name} is from {city}, and he likes {cake} cake, {fruit}"
          " fruit, {salad} salad, and {pasta} pasta".format(**info_dict))


def hex_gen():
    """
    Generates and displays two dictionaries, one using a list comprehension
    and the other using a dict comprehension.
    """
    hex_list = [hex(x) for x in range(16)]
    new_dict = dict(zip(range(16), hex_list))
    hex_dict = {x: hex(x) for x in range(16)}
    print(new_dict)
    print(hex_dict)


def a_counter(info_dict):
    """
    Take in a dictionary and display a new dict with values representing the
    number of 'a's in the input dictionary's values.
    """
    new_dict = {key: value.count('a') for (key, value) in info_dict.items()}
    print(new_dict)


def set_gen():
    """
    Create three sets based on the divisors of 2, 3 and 4. Display each set.
    """
    s2 = {x for x in range(21) if x % 2 == 0}
    s3 = {x for x in range(21) if x % 3 == 0}
    s4 = {x for x in range(21) if x % 4 == 0}
    print(s2, s3, s4)


def generalized_set_gen(divisors):
    """
    Take in a list of integers and return a list of integer sets.
    """
    set_list = []
    for divisor in divisors:
        comp = [x for x in range(21) if x % divisor == 0]
        set_list.append(comp)
    return set_list


def generalized_set_gen2(divisors):
    """
    Take in a list of integers and return a list of integer sets.
    Question: Output is correct but in a single list. How would I seperate the
    output into multiple lists?
    """
    return [x for d in divisors for x in range(21) if x % d == 0]


# ==============================================================================


def main():
    """
    Tests output.
    """
    info_dict = {"name": "Chris",
                 "city": "Seattle",
                 "cake": "Chocolate",
                 "fruit": "mango",
                 "salad": "greek",
                 "pasta": "lasagna"}
    divisors = [2, 3, 4, 5, 8]
    # part1(info_dict)
    # print(part2(info_dict))
    # part3()
    # part4()
    # display_dict(info_dict)
    a_counter(info_dict)
    # hex_gen()
    # set_gen()
    # print(generalized_set_gen(divisors))
    # print(generalized_set_gen2(divisors))


if __name__ == '__main__':
    main()
