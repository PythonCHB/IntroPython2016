# !/usr/bin/env python3
"""
Name: Paul Briant
Date: 10/24/16
Class: Introduction to Python
Session04
LAB: Dictionaries

Description:
This lab explores various ways of utilizng dictionaries, sets and their
associated methods.
"""
# -------------------------------Import-----------------------------------------

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


# ==============================================================================


def main():
    """
    Tests output.
    """
    dict1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
    # part1(dict1)
    print(part2(dict1))
    # part3()
    # part4()


if __name__ == '__main__':
    main()
