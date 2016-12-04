#!/usr/bin/env python3

# Keyword Lab
# Apologies for the length of this one

'''
Keyword arguments:

Write a function that has four optional parameters (with defaults): fore_color
back_color link_color visited_color Have it print the colors (use strings for
the colors) Call it with a couple different parameters set using just positional
arguments: func('red', 'blue', 'yellow', 'chartreuse') using just keyword
arguments: func(link_color='red', back_color='blue') using a combination of
positional and keyword ``func('purple', link_color='red', back_color='blue')
using *some_tuple and/or **some_dict regular = ('red', 'blue') links =
{'link_color': 'chartreuse'} func(*regular, *links) Generic parameters:

Write a the same function with the parameters as: *args and **kwags

Have it print the colors (use strings for the colors) Call it with the same
various combinations of arguments used above. Also have it print args and kwargs
directly, so you can be sure you understand what’s going on. Note that in
general, you can’t know what will get passed into **kwargs So maybe adapt your
function to be able to do something reasonable with any keywords.

---

Think Python [Chapter 12  Tuples]
A parameter name that begins with * gathers arguments
The complement of gather is scatter. If you have a sequence of values and you 
want to pass it to a function as multiple arguments, you can use the * operator.

http://stackoverflow.com/questions/3394835/args-and-kwargs
You would use *args when you're not sure how many arguments might be passed to
your function, i.e. it allows you pass an arbitrary number of arguments to
your function.
Similarly, **kwargs allows you to handle named arguments that you have not
defined in advance
'''

# Think Python: 12.4  Variable-length argument tuples
# http://www.greenteapress.com/thinkpython/html/thinkpython013.html

'''Write a function called sumall that takes any number of arguments and returns
their sum.'''

def sumall(*args):
    total = 0
    for entry in args:
        total += entry
    return total

print('\nThink Python: 12.4 > sumall')
print('sumall(1, 2, 3)', sumall(1, 2, 3))
print('sumall(10, 16, 33, 11, 9, 123)', sumall(10, 16, 33, 11, 9, 123))
print('sumall(1, 7, 3, 15, 22, 74, 21, 2)', sumall(1, 7, 3, 15, 22, 74, 21, 2))

# ---

# positional
# keyword
# combination

def positional_args(x,y):
    print('x = ', x, 'y = ', y)
# positional_args(3, 7)
#   x =  3 y =  7

print(colors_positional('Orange', 'Green', 'Indigo', 'Violet'))

# print(colors_positional('Orange', 'Green', 'Indigo'))
# TypeError: colors_positional() missing 1 required positional argument: 'visited_color'

# ---

# Adding "default" values
def default_args(x = 3, y = 4):
    print('x = ', x, 'y = ', y)
# This actually defines key/value pairs
# Now position is *optional*
# default_args(7, 10)
#   x =  7 y =  10
# default_args(y = 22)
#   x =  3 y =  22

print(default_args(7, 10))
print(default_args(y = 12))
print(default_args(x = 32))
print(default_args(1, y = 75))

# print(default_args(64, x = 12))
# TypeError: default_args() got multiple values for argument 'x'

# print(default_args(x = 1, 75))
# SyntaxError: positional argument follows keyword argument

# ---

def colors_positional(fore_color, back_color, link_color, visited_color):
    print('''
        \n\tfore_color = {}
        \n\tback_color = {}
        \n\tlink_color = {}
        \n\tvisited_color = {}'''.format(fore_color, back_color, link_color, visited_color))
        
print(colors_positional('Purple', 'Green', 'Black', 'White'))

# print(colors_positional('Purple', 'Green', 'Black'))
# TypeError: colors_positional() missing 1 required positional argument: 'visited_color'

# print(colors_positional('Purple', 'Green', 'Indigo', 'Black', 'White'))
# TypeError: colors_positional() takes 4 positional arguments but 5 were given

# ---

def colors_keywords(fore_color = 'Pink', back_color = 'Red', link_color = 'Green', visited_color = 'Indigo'):
    print('''
        \n\tfore_color = {}
        \n\tback_color = {}
        \n\tlink_color = {}
        \n\tvisited_color = {}'''.format(fore_color, back_color, link_color, visited_color))

print(colors_keywords('Yellow', 'Cyan', 'White', 'Black'))
print(colors_keywords('Orange', 'Green', 'Indigo', 'Violet'))
print(colors_keywords('Orange', 'Green', 'Indigo'))
print(colors_keywords('White', visited_color = 'Yellow', back_color = 'Cyan'))

# print(colors_keywords(visited_color = 'Yellow', back_color = 'Cyan', 'White', 'Black'))
# SyntaxError: positional argument follows keyword argument

# print(colors_keywords('White', 'Black', visited_color = 'Yellow', back_color = 'Cyan'))
# TypeError: colors_keywords() got multiple values for argument 'back_color'

# ---

# Brute force - this doesn't seem very useful
# This makes sense to me to use with values, but not strings
# Create default color values, then overwrite them with args (if present)
# Positional overwrite of default values
def colors_args(*args):
    fore_color, back_color, link_color, visited_color = 'Mud', 'Mud', 'Mud', 'Mud'
    print('len(args) =', len(args))
    if len(args) == 1:
        fore_color = args[0]
    elif len(args) == 2:
        fore_color = args[0]
        back_color = args[1]
    elif len(args) == 3:
        fore_color = args[0]
        back_color = args[1]
        link_color = args[2]
    elif len(args) >= 4:
        fore_color = args[0]
        back_color = args[1]
        link_color = args[2]
        visited_color = args[3]
    print('''
        \n\tfore_color = {}
        \n\tback_color = {}
        \n\tlink_color = {}
        \n\tvisited_color = {}'''.format(fore_color, back_color, link_color, visited_color))

print(colors_args('Indigo', 'Violet'))
print(colors_args('Indigo', 'Violet', 'Green', 'White', 'Magenta'))

# ---

# CHB lecture notes
def f(x, y, w=0, h=0):
    print("position: {}, {} -- shape: {}, {}".format(x, y, w, h))

position = (3,4)
size = {'h': 10, 'w': 20}

f(*position, **size)
# position: 3, 4 -- shape: 20, 10

# ---

# CHB lecture notes
def f(*args, **kwargs):
    print("the positional arguments are:", args)
    print("the keyword arguments are:", kwargs)
    print(type(args))
    print(type(kwargs))

f(2, 3, this=5, that=7)
# the positional arguments are: (2, 3)
# the keyword arguments are: {'this': 5, 'that': 7}

# ---

# naming keys ('fore_color' : 'Mud') vs kwargs (fore_color = 'Blue')
#   vs .format variables ({fore_color}) really tripped me up here
# Now it looks simple, but: arrrrrgghhh!
def colors_kwargs(**kwargs):
    default_dictionary = {'fore_color' : 'Mud',
                            'back_color' : 'Mud',
                            'link_color' : 'Mud',
                            'visited_color' : 'Mud'}
    for entry in kwargs:
#         print(entry, kwargs[entry])
        default_dictionary[entry] = kwargs[entry]
    print('''
        \n\tfore_color = {fore_color}
        \n\tback_color = {back_color}
        \n\tlink_color = {link_color}
        \n\tvisited_color = {visited_color}'''.format(**default_dictionary))

fullcolor_dictionary = {'fore_color' : 'Brown',
                    'back_color' : 'Green',
                    'link_color' : 'Cyan',
                    'visited_color' : 'Blue'}
                    
partialcolor_dictionary = {'fore_color' : 'Brown',
                    'visited_color' : 'Blue'}

overloadedcolor_dictionary = {'fore_color' : 'Brown',
                    'accent_color' : 'Violet',
                    'imaginary_color' : 'Yellow',
                    'back_color' : 'Green',
                    'link_color' : 'Cyan',
                    'visited_color' : 'Blue'}

print(colors_kwargs(fore_color = 'Blue'))
print(colors_kwargs(**fullcolor_dictionary))
print(colors_kwargs(**partialcolor_dictionary))
print(colors_kwargs(**overloadedcolor_dictionary))

# print(colors_kwargs('Blue'))
# TypeError: colors_kwargs() takes 0 positional arguments but 1 was given

# ---

# Making sense of things
def args_test(*args):
    print(type(args))
    for entry in args:
        print(type(entry))