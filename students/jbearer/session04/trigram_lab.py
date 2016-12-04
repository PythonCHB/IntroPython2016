#!/usr/bin/env/python3
"""
LAB: Trigrams
October 20, 2016
"""

import random

def trigram_fun():
    with open('sherlock.txt','r') as file_in:
        my_book = file_in.read()

    my_book = my_book.replace('\n', ' ').strip()

    l_book = my_book.split()

    trigram_list = zip(l_book,l_book[1:], l_book[2:])

    # Builds the dictionary keys and values from the file.
    dict_list = {}
    for first, second, third in trigram_list:
        key = ' '.join((first, second))
        dict_list.setdefault(key, []).append(third)
    
    # Starts building the list of words to use in the paragraph
    new_tri = []
    myStr = list(dict_list.keys())[0]
    new_tri.extend(myStr.split())

    for i in range(150):
        myStr = ' '.join(new_tri[-2:])

        if myStr not in dict_list:
            # Will add new key and value as empty list
            print('myStr:', myStr)
            print('no key in dict')
        else:
            new_tri.append(random.choice(dict_list[myStr]))

    """ Start building something that looks like a paragraph of text
        and strip unneeded characters from words.  Add capitalization
        and a period at the end of each sentance.
    """

    exclude = set('./"!?\'')

    for i in range(len(new_tri)):
        myWord = new_tri[i]
        myWord = ''.join(ch for ch in myWord if ch not in exclude)
        if i % 13 == 0:
            myWord = myWord.capitalize()
            print(myWord, end=' ')
        elif i % 13 == 12:
            myWord = myWord.lower() + '.'
            print(myWord, end=' ')
        else:       
            myWord = myWord.lower()
            print(myWord, end=' ')
    print() 

trigram_fun()