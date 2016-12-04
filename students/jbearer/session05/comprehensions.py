
def list_comp():
    
    feast = ['lambs', 'sloths', 'orangutans','breakfast cereals', 'fruit bats']

    comprehension = [delicacy.capitalize() for delicacy in feast]

    print('comprehension:', comprehension)

    comp = [delicacy for delicacy in feast if len(delicacy) > 6]

    print('len of feast:', len(feast))
    print('len of comp:', len(comp))

# list_comp()

def tuples_comp():

    list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

    comprehension = [skit * number for number, skit in list_of_tuples]

    print('comprehension:', comprehension[0])
    print('len of comprehension:', len(comprehension[2]))

# tuples_comp()

def double_list_comp():
    
    eggs = ['poached egg', 'fried egg']
    meats = ['lite spam', 'ham spam', 'fried spam']
    comprehension = ['{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]

    print('len of comprehension:',len(comprehension))
    print('comprehension[0]',comprehension[0])

# double_list_comp()

def set_comp():
    comprehension = { x for x in 'aabbbcccc'}
    print(comprehension)

# set_comp()

def dict_comp():
    dict_of_weapons = {'first': 'fear',
                       'second': 'surprise',
                       'third':'ruthless efficiency',
                       'forth':'fanatical devotion',
                       'fifth': None}
    dict_comprehension = {k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

    print('first' in dict_comprehension)
    print('FIRST' in dict_comprehension)
    print('len of dict_of_weapons:', len(dict_of_weapons))
    print('len of dict_comprehension:', len(dict_comprehension))

# dict_comp()

# COUNT EVEN NUMBERS #
def count_evens(nums):
    comp = [myNum for myNum in nums if myNum % 2 == 0]
    return len(comp)

# print('>>>Count even numbers <<<')
# print(count_evens([2, 1, 2, 3, 4]))
# print(count_evens([2, 2, 0]))
# print(count_evens([1, 3, 5]))
# print()

print('>>> Dict and Set Comprehension <<<')

def dict_comp():
    
    food_prefs = {"name": "Chris", "city": "Seattle", "cake": "chocolate",
                    "fruit": "mango", "salad": "greek", "pasta": "lasagna"}

    #1.
    dict_answer = ['{} is from {}, and he likes {} cake, {} fruit, {} salad, and {} pasta.'.format(food_prefs['name'],food_prefs['city'],food_prefs['cake'],food_prefs['fruit'],food_prefs['salad'],food_prefs['pasta'])]
    # print(dict_answer)

    #2.
    num_list = [myNum for myNum in range(16)]
    hex_list = [hex(myHex) for myHex in range(16)]
    num_hex_list = list(zip(num_list, hex_list))
    num_hex_list2 = [(myNum, hex(myHex)) for (myNum, myHex) in range(16)]
    print(num_hex_list2)
    # print(num_hex_list)

    #3.
    new_dict = {myInt: myHex for (myInt, myHex) in num_hex_list}
    # print(new_dict)

    #4.
    dict_food_a = {k: v.count('a') for (k, v) in food_prefs.items()}
    # print(dict_food_a)

    #5a.
    s2 = {div_2 for div_2 in range(21) if div_2 % 2 == 0}
    s3 = {div_3 for div_3 in range(21) if div_3 % 3 == 0}
    s4 = {div_4 for div_4 in range(21) if div_4 % 4 == 0}
    # print(s2)
    # print(s3)
    # print(s4)

    #5.b.a
    s5 = s2.union(s3, s4)
    # print(s5)
    
    #5.b.b
    # Not sure what it means to 'build the set up'.

    #5.b.c (incomplete)
    s6 = {div_num for div_num in range(21) if div_num % 2 == 0 or div_num % 3 == 0 or div_num % 4 == 0}
    print(s6)

dict_comp()
