#!/usr/bin/env/python3
"""
LAB: Key Arguments
November 1, 2016
"""

def colors(fore_color='Red', back_color='White',
    link_color='Blue', visited_color='Green'):
    
    print('Fore: {} \nBack: {} \nLink: {} \nVisit: {}'.format(fore_color,
        back_color, link_color, visited_color))


t = ('Purple', 'Yellow', 'Pink', 'Brown')

d = {'fore_color': 'Black', 'back_color': 'Tan',
    'link_color': 'Gray', 'visited_color': 'Teal'}

if __name__ == '__main__':
    colors()
    print()
    colors(*t)
    print()
    colors(**d)