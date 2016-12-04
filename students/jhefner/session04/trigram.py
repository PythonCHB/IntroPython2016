#!/Users/jhefner/python_dev/uw_python/bin/python

import json #just used to pretty print the dictionary when I was debugging
import random

"""
Thoughts on how im going to do this:
---
How to store the data: a dictionary.
Key = First two words (starting at position 0,1 in line of document and incrementing to end of line
Value = list. list is populated with each the 2 words that come after the key. This will retain only unique matches without incurring overhead of duplicate checking.

The method for creating the dictionary:
Bring entire file into memory if possible. If it looks like the file is too big I'll have to evaluate it line by line.
Split entire file or each line as mentioned above ^ so it is now a long list.
Start at (0,1) of list and define it as the key, add (2) of list to list.
Increment list position to key(1,2) and list(3) and so on.

That will generate my dictionary to make up a new novel with.

Generating the text file:
1. To choose an arbitrary starting point use rand to choose a random dictionary key that has that as the first word in the key.
2. Take Key and append to output.
3. Use rand to choose a random value from keys list and append to output.
4. Evaluate last word in output, find rand dictionary key sthat starts with the word.
5. Step 2-4 until done.
"""

def read_file_to_memory(filename):
    with open(filename) as f:
        file_data = f.read()
        return file_data

def create_trigram_dictionary(file_data):
    listerizer = file_data.split()
    trigram_dictionary = {}
    for i in range(len(listerizer)-2):
        key = listerizer[i] + " " + listerizer[i+1]
        val = listerizer[i+2]
        trigram_dictionary.setdefault(key,[]).append(val)
    return trigram_dictionary

def create_trigram_book(trigram_dictionary):
    random_starting_key = random.choice(list(trigram_dictionary.keys()))
    words_list = " ".join((random_starting_key,random.choice(trigram_dictionary[random_starting_key]))).split()
    phrase = " ".join((words_list[-2],words_list[-1]))
    # print("word list:",words_list)
    # print("phrase:",phrase)
    # print("phrase type:",type(phrase))
    # print("phrase in trigram dict:",phrase in trigram_dictionary)

    while phrase in trigram_dictionary:
        words_list.append(random.choice(trigram_dictionary[phrase]))
        phrase = " ".join((words_list[-2],words_list[-1]))

    book = " ".join((words_list))
    return book


def main():
    file_data = read_file_to_memory('sherlock.txt')
    trigram_dictionary = create_trigram_dictionary(file_data)
    # print(json.dumps(trigram_dictionary, indent=4))
    # print(trigram_dictionary)
    new_book = create_trigram_book(trigram_dictionary)
    print("--------------------BOOK--------------------\n"+new_book)

if __name__ == '__main__':
    main()