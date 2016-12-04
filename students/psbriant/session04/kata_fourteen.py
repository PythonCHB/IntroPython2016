"""
Name: Paul Briant
Date: 10/24/16
Class: Introduction to Python
Session04
Assignment: Kata Fourteen

Description:
Read a file and build a trigram based off of the text in file.
"""
# -------------------------------Import-----------------------------------------
import random
# -------------------------------Functions--------------------------------------


def read_file(file_name):
    """
    Take in a file and return it as a string.
    """
    with open(file_name) as f:
        string = f.read()
    return string


def gen_list(string):
    """
    Take in a large string of all the words in the file. Split that string
    into a list of strings.
    """
    str_list = string.split()
    return str_list


def dict_gen(str_list):
    """
    Take in a list of strings. Iterate through list of strings and concatenate
    focus item and item directely following it to create a dictionary key.
    Assign the next string as the value. Return dictionary.
    """
    tri_dict = {}

    for i in range(len(str_list)):
        # Ensures list index is in range
        if (i + 2) < len(str_list):
            # Use the first two strings as a key in tri_dict.
            tri_key = str_list[i] + ' ' + str_list[i + 1]
            # Check if key exists
            if tri_key not in tri_dict.keys():
                # Use the third string as the value tri_dict.
                tri_dict[tri_key] = [str_list[i + 2]]
            else:
                # If key already exists, add new values.
                tri_dict[tri_key].append(str_list[i + 2])
    return tri_dict


def key_lookup(str_list):
    """
    Once entire file has been iterated through:
    Choose random word pair as the start and use these to look up the next
    word.
    """
    rand_item = random.choice(str_list)
    item2_index = str_list.index(rand_item) + 1
    item2 = str_list[item2_index]
    start_key = rand_item + ' ' + item2
    return start_key


def build_trigram(str_key, tri_dict):
    """
    Create a list of strings to write to a new file.
    Use random key as the first string and append it to the list.
    Use it to lookup the next string.
    Split the first string and use the second and third strings to look up the
    next string.
    If a key has multiple values, choose a random value.
    """
    # Strings to write to file
    out_list = []
    # Current key
    key_phrase = str_key
    # Add element to out list
    out_list.append(key_phrase)

    # import pdb; pdb.set_trace()
    while True:

        if key_phrase not in tri_dict:
            break
        # Get the next string
        next_str = tri_dict[key_phrase]
        if len(next_str) > 1:
            # Add random element to list
            out_list.append(random.choice(next_str))
        else:
            # Add to list
            out_list.extend(next_str)
        # Assign new strings to key phrase
        key_phrase = key_phrase.split()
        key_phrase = key_phrase[1] + ' ' + out_list[-1]
    return out_list


def write_file(trigram):
    """
    Take in a list of strings representing the trigram. Join list into one
    string and write to a new file.
    """
    # text = " ".join(trigram)
    lines = []
    with open('new_trigram.txt', 'w') as outfile:
        for string in trigram:
            if len(lines) > 8:
                text = " ".join(lines) + '\n'
                outfile.write(text)
                lines = []
            else:
                lines.append(string)
        text = " ".join(lines) + '\n'
        outfile.write(text)
    outfile.close()

# ==============================================================================


def main():
    """
    Calls methods and builds a trigram based on an input file.
    """
    string = read_file('sherlock_small.txt')
    str_list = gen_list(string)
    tri_dict = dict_gen(str_list)
    str_key = key_lookup(str_list)
    trigram = build_trigram(str_key, tri_dict)
    write_file(trigram)


if __name__ == '__main__':
    main()
