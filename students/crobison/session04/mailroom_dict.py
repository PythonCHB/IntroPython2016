#!/usr/bin/env python3

# Charles Robison
# 2016.11.09
# Mailroom using dictionary
# Using professor's answers for review...

from textwrap import dedent
import math
import sys

def get_donor_db():
    return {'smith': ('Smith', [100, 125, 100]),
            'galloway': ('Galloway',[50]),
            'williams': ('Williams',[22, 43, 40, 3.25]),
            'cruz': ('Cruz',[101]),
            'maples': ('Maples',[1.50, 225]),
            }

def list_donors(): # this part doesn't seem to be working...why?
    listing = ["Donor list:"]
    for donor in donor_db.values():
        listing.append(donor[0])
    return "\n".join(listing)

# def print_donors(): # copied from Barker file
#     print("Donor list:\n")
#     for donor in donors:
#         print(donor[0])

def find_donor(name): # copied from Barker file
    key = name.strip().lower()
    return donor_db.get(key)

def add_donor(name):
    name = name.strip()
    donor = (name, [])
    donor_db[name.lower()] = donor
    return donor

def main_menu_selection():
    action = input(dedent('''
        Choose an action:

        1 - Send a Thank You
        2 - Create a Report
        3 - Quit

        > '''))
    return action.strip()

# def sort_key(item): # copied from Barker file.  What does this do?
#     return item[1]

def generate_donor_report():
    report_rows = [] # copied from Barker file
    for (name, gifts) in donor_db.values():
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))
    report_rows.sort(key=sort_key, reverse=True)
    print("{:25s} | {:11s} | {:9s} | {:12s}".format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 66)
    for row in report_rows:
        print("{:25s}  ${:11.2f}   {:9d}  ${:12.2f}".format(*row))

def gen_letter(donor):
    return dedent('''
        Dear {0:s},

        Thank you for your very kind donation of ${1:.2f}.
        It will be put to very good use.

                        Sincerely,
                           -The Team
       '''.format(donor[0], donor[1][-1]))

def send_thanks(): # copied from Barker file
    print("This will write a thank you note")
    while True: # the rest of this copied from Barker file
        name = input("Enter a donor's name "
            "(or 'list' to see all donors or 'menu' to exit)> ").strip()
        if name == 'list':
            list_donors()
        elif name == 'menu':
            return
        else:
            break
    while True:
        amount_str = input("Enter a donation amount(or 'menu' to exit) > ").strip()
        if amount_str == "menu":
            return
        amount = float(amount_str)
        if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
            continue
        else:
            break
    donor = find_donor(name)
    if donor is None:
        donor = (name, [])
        donors.append(donor)
    donor[1].append(amount)
    print(gen_letter(donor))

def sort_key(item):
    return item[1]

def quit():
    sys.exit(0)

if __name__ == "__main__":
    donor_db = get_donor_db()
    running = True
    selection_dict = {"1": send_thanks,
                      "2": generate_donor_report,
                      "3": quit}

    while True:
        selection = main_menu_selection()
        try:
            selection_dict[selection]()
        except KeyError:
            print("error: menu selection is invalid!")
