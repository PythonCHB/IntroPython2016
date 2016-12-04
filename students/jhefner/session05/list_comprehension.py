#!/Users/jhefner/python_dev/uw_python/bin/python

def main():
    # List comprehensions
    feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
    comprehension = [delicacy.capitalize() for delicacy in feast]
    # this looks like its going to define an interable variable 'delicacy'.
    # its going to iterate apply the .capitalize() function on it (which will capitalize just the first letter of a word
    # its going to do this `for delicacy in feast`, as in its going to use a for loop to go through the while list
    print(comprehension)
    # yup looks like it did like I guessed.

    print(comprehension[0])
    # hmnnn, calling the zero'th element of this list should just return the capitalized word 'Lambs".
    # yup looks like it returned it as a string.

    print(comprehension[2])
    # same setup as above, should call the 2th element (3rd if you count like human) in the list.
    # So the capitalized 'Orangutans' word.



    # Filtering lists with list comprehensions
    feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals','fruit bats']
    comp = [delicacy for delicacy in feast if len(delicacy) > 6]

    print(len(feast))
    # Should be 5, we are just looking in the original list for its length.
    # Which would be the # of elements it has.

    print(len(comp))
    # This should be 3. Only 3 words in the list of words (feast) are more than 6 characters.
    # Namely 'orangutans', 'breakfast cereals', 'fruit bats'



    # Unpacking tuples in list comprehensions
    list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
    comprehension = [ skit * number for number, skit in list_of_tuples ]

    print(comprehension[0])
    # ok this is interesting. we are returning the 0th element of the multiplied list of skit*number.
    # the 0th element is the (1, 'lumberjack'). since 1x'lumberjack' shoudl just be 'lumberjack' thats what we get.

    print(len(comprehension[2]))
    # ok spam*4 is the word spam 4 times. so the length of that string should be 11 (since we are counting from 0.

    # haha ok i got this wrong. i did 4 characters (spam) *3 instead of 4 as the length then minused one because i thought length included 0.
    # apparently its 16, which 4*4 = 16 so apparently len doesn't count using 0. Which i guess makes sense.



    # Double list comprehensions
    eggs = ['poached egg', 'fried egg']
    meats = ['lite spam', 'ham spam', 'fried spam']
    comprehension = [ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]

    print(len(comprehension))
    # this one is hard....haha. so the .format makes me think its gonna return a tuple...
    # ok im not quite sure whats gonna happen here. if i had to guess
    # its going to turn each element of each list of items into a tuple of the 1st and 2nd element from that list.
    # so comprehension would become a combination of both elements of eggs/meats and look sorta like:
    #  comprehension = ('poached egg', 'fried egg'), ('lite spam', 'ham spam').....fuu actually im not sure...
    # this one has 3 elements...

    print(comprehension[0])
    # no idea...

    # OHHHh so it was doing basically what ZIP was doing the other day.
    # this is just a manual way of seeing that happen.
    # nice!



    #Dictionary comprehensions
    dict_of_weapons = {'first': 'fear',
                       'second': 'surprise',
                       'third':'ruthless efficiency',
                       'forth':'fanatical devotion',
                       'fifth': None}
    dict_comprehension = { k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

    print('first' in dict_comprehension)
    # i believe it will return "FEAR" since it evaluates to true that there is a weapon assigned to that key.
    # and it is gonna call upper on that element.

    # OH WAIT its already capitalized so it should error out or something...i think.

    print('FIRST' in dict_comprehension)
    # ok this one should read "fear" since the upper function was only called on the keys not the values.

    print(len(dict_of_weapons))
    # 5, there are 5 keys in the dictionary so thats what it counts when you iterate over a dictionary.

    print(len(dict_comprehension))
    # 4, since the "fifth" key's value does not evaluate to true it wont be included in the new dictionary being created.






if __name__ == '__main__':
    main()