#! /usr/bin/env python

import random

# Global Variables #

input_text = input("Please enter a two word text string from the document '\n'"
                   "> ")
input_text = input_text.split()  # convert input_text to list #
matches_list = []  # Container for word(s) that follow input text #

# Open file, get rid of breaks, and return as list #

with open('/Users/SMcGhin/Documents/IntroPython2016/students/spencer_mcghin/session4/sherlock_small.txt', 'r') as text:
    doc_list = text.read().lower().strip('--').split() # Generate List #
    doc = [" ".join(doc_list).strip('--')]  # Make one long string #


# Validate input against text list and generate following words #


def gen_trigrams():
    for i in range(0, len(doc_list) - 3):  # iterate through the document and find matches for each part of input_text #
        if input_text[0] == doc_list[i] and input_text[1] == doc_list[i + 1]:
            matches_list.append(doc_list[i + 2])  # Append matching values to list object #
    input_text.append(random.choice(matches_list))  # Add input text and appended values to make one list #
    print(matches_list)
    print(input_text)

# Take Last Two Indexes of gen_trigrams() and perform same operation #


def print_story():
    trigrams = gen_trigrams()
    first_value = trigrams[-2]
    second_value = trigrams[-1]
    for i in range(0, len(doc_list) - 3):
        if first_value == doc_list[i] and second_value == doc_list[i + 1]:
            values_list.append(doc_list[i + 2])
    print(first_value)
    print(second_value)

gen_trigrams()
