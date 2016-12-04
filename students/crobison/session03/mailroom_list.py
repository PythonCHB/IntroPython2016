# Charles Robison
# 2016.10.16
# Mailroom Lab

# New version using list instead of dictionary

#!/usr/bin/env python

from textwrap import dedent
import math

donors = [
            ('Smith', [100, 125, 100]),
            ('Galloway',[50]),
            ('Williams',[22, 43, 40, 3.25]),
            ('Cruz',[101]),
            ('Maples',[1.50, 225])
         ]

# donations = {}
# for k, v in donors.items():
#     donations[k] = sum(v)

def print_donors(): # copied from Barker file
    print("Donor list:\n")
    for donor in donors:
        print(donor[0])

def find_donor(name): # copied from Barker file
    for donor in donors:
        if name.strip().lower() == donor[0].lower():
            return donor
    return None # why here instead of else statement?

def sort_key(item): # copied from Barker file.  What does this do?
    return item[1]

def print_report():
    report_rows = [] # copied from Barker file
    for (name, gifts) in donors:
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
        Dear {}

        Thank you for your very kind donation of ${:.2f}.
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
            print_donors()
        elif name == 'menu':
            return
        else:
            break
    while True:
        amount_str = input("Enter a donation amount(or 'menu' to exit) > ").strip()
        if amount_str == "menue":
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


# here is where triple quoted strings can be helpful
msg = """
What would you like to do?
To send a thank you: type "s"
To print a report: type "p"
To exit: type "x"
"""


def main():
    """
    run the main interactive loop
    """

    response = ''
    # keep asking until the users responds with an 'x'
    while True:  # make sure there is a break if you have infinite loop!
        print(msg)
        response = input("==> ").strip()  # strip() in case there are any spaces

        if response == 'p':
            print_report()
        elif response == 's':
            send_thanks()
        elif response == 'x':
            break
        else:
            print('please type "s", "p", or "x"')

if __name__ == "__main__":
    main()