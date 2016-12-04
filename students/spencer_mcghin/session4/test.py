import random

# Global Variables #

input_text = input("Please enter a text string from the document '\n'"
                   "> ")
input_text = input_text.split()  # convert input_text to list #
tri_list = [input_text]

# Open file, get rid of breaks, and return as list #

with open('/Users/SMcGhin/Documents/IntroPython2016/students/spencer_mcghin/session4/sherlock_small.txt', 'r') as text:
    doc_list = text.read().split()  # Generate List #
    doc = [" ".join(doc_list).strip('--')]  # Make one long string #


# Validate input against text list and generate following words #


def gen_trigrams():
    for i in range(0, len(doc_list) - 3):  # iterate through the document and find matches for each part of input_text #
        if input_text[0] == doc_list[i] and input_text[1] == doc_list[i + 1]:
            tri_list.append([doc_list[i + 2]])  # Append matching values to list object #
            test_rand = random.choice(doc_list[i + 2])
    final_list = (list(sum(tri_list, [])))  # Add input text and appended values to make one list #
    print(test_rand)


gen