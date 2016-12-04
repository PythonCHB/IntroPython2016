"""
Name: Paul Briant
Date: 11/15/16
Class: Introduction to Python
Session05
LAB: Args

Description:
This Lab explores the various ways to call function arguments including passing
tuples and dictionaries and unpacking them using args and kwargs.
"""

# -------------------------------Imports----------------------------------------


# -------------------------------Functions--------------------------------------


def print_colors(fore_color='Blue', back_color='Green', link_color='White',
                 visited_color='Yellow'):
    """
    Take in strings representing the color of the foreground, background, links
    and visited links of a website and display the them.
    """
    print("Foreground: {fore_color} Background: {back_color} Links:"
          " {link_color} Visited links: {visited_color}"
          "".format(fore_color=fore_color, back_color=back_color,
                    link_color=link_color, visited_color=visited_color))


def print_colors2(**kwargs):
    """
    Take in strings representing the color of the foreground, background, links
    and visited links of a website and display the them.
    """
    print("Foreground: {fore_color} Background: {back_color}"
          " Links: {link_color} Visited"
          " links: {visited_color}".format(**kwargs))


def print_colors3(*args):
    """
    Take in strings representing the color of the foreground, background, links
    and visited links of a website and display the them.
    """
    print("Foreground: {} Background: {}"
          " Links: {} Visited"
          " links: {}".format(*args))


# ==============================================================================


def main():
    """
    Calls functions and produces output.
    """
    print_colors()
    print_colors('Purple')
    print_colors(back_color='Black', visited_color='Pink')
    args1 = ('Blue', 'Red', 'Teal')
    args2 = ('Pink', 'Orange', 'Teal', 'Gold')
    dict1 = {'fore_color': 'Black',
             'back_color': 'Green',
             'link_color': 'Red',
             'visited_color': 'Yellow'}
    print_colors(*args1)
    print_colors(*args2)
    print_colors(**dict1)
    # print_colors2(fore_color='Blue', back_color='Green', link_color='White',
    # visited_color='Yellow')
    # print_colors3('Black', 'Pink', 'Blue', 'Yellow')


if __name__ == '__main__':
    main()
