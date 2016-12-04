#!/Users/jhefner/python_dev/uw_python/bin/python
"""
LAB
Keyword arguments:

Write a function that has four optional parameters (with defaults):
fore_color
back_color
link_color
visited_color
Have it print the colors (use strings for the colors)
Call it with a couple different parameters set
using just positional arguments:
func('red', 'blue', 'yellow', 'chartreuse')
using just keyword arguments:
func(link_color='red', back_color='blue')
using a combination of positional and keyword
``func('purple', link_color='red', back_color='blue')
using *some_tuple and/or **some_dict
regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}
func(*regular, *links)
Generic parameters:

Write a the same function with the parameters as:
*args and **kwags

Have it print the colors (use strings for the colors)
Call it with the same various combinations of arguments used above.
Also have it print args and kwargs directly, so you can be sure you understand what’s going on.
Note that in general, you can’t know what will get passed into **kwargs So maybe adapt your function to be able to do something reasonable with any keywords.
"""

def colors(
    fore_color="yellow",
    back_color="blue",
    link_color="black",
    visited_color="green"):
    print("\n"+fore_color,"\n"+back_color,"\n"+link_color,"\n"+visited_color)

def colors2(*args,**kwargs):
    if args: print(args)
    if kwargs: print(kwargs)
    print("\n",*args,"\n",**kwargs)


def main():
    colors()
    colors('red','blue','yellow','chartreuse')
    colors(link_color='red', back_color='blue')
    colors('purple', link_color='red', back_color='blue')
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    colors(*regular, *links)

    colors2()
    colors2('red','blue','yellow','chartreuse')
    colors2(link_color='red', back_color='blue')
    colors2('purple', link_color='red', back_color='blue')
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    colors2(*regular, *links)


if __name__ == '__main__':
    main()