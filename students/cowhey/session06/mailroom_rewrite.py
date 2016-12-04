#!/usr/bin/env python3

import sys

donors = {"Wilmot Filipe": [18.00, 72.00],
          "Neoptolemus Yaropolk": [36.00],
          "Mahesha Diogenes": [90.00, 54.00, 18.00],
          "Arthur Tjaz": [18.00],
          "Luuk Sinclair": [180.00]}


def end_program():
    sys.exit(0)


def accept_donation():
    while True:
        amount = input("How much did this person donate? \n")
        if amount.strip().lower() == "x":
            return
        try:
            float(amount)
            return float(amount)
        except:
            print("You must enter a numeric amount.")


def create_reports():
    donor_rows = [[donor,
                   "{:.2f}".format(sum(donors[donor])),
                   str(len(donors[donor])),
                   "{:.2f}".format((sum(donors[donor])) / len(donors[donor]))]
                  for donor in donors.keys()]
    return donor_rows


def format_row(row):
    formatted = []
    for item in row:
        formatted.append('{:30}'.format(item))
    return ' '.join(formatted)


def print_donor_list():
    print("These are the donors you have in your database:")
    for donor in donors:
        print(donor)
    print()


def print_report():
    print("This will print a report")
    header_row = ["Name",
                  "Total Donated",
                  "Number of Donations",
                  "Average Donation"]
    donor_rows = create_reports()
    donor_rows.sort(key=total_donation_amount, reverse=True)
    print(format_row(header_row))
    for row in donor_rows:
        print(format_row(row))
    print()


def send_thanks():
    print("This will write a thank you note")
    # donor_names = list(donors.keys())
    thank_you_command = input("Type the full name of the person you would like to thank. \nOr type 'list' to see a list of donors.\n")
    if thank_you_command.lower().strip() == "x":
        return
    elif thank_you_command.lower().strip() == "list":
        print_donor_list()
    else:
        donation_amount = accept_donation()
        if not donation_amount:
            return
        if thank_you_command in donors:
            name = thank_you_command
            donors[name].append(donation_amount)
            print("Adding ${:02.2f} to {}'s donations."
                  .format(donation_amount, name))
            print_thank_you(name)
        else:
            print(donation_amount)
            name = thank_you_command
            donors[name] = [donation_amount]
            print("Adding {} as a donor, with a donation of ${:02.2f}."
                  .format(name, donation_amount))
            print_thank_you(name)


# here is where triple quoted strings can be helpful
msg = """
What would you like to do?

To send a thank you: type "s"
To print a report: type "p"
To write thank yous to all donors: type "w"
To exit: type "x"
"""


def main():
    """
    run the main interactive loop
    """
    response = ""
    # keep asking until the users responds with an 'x'
    while True:  # make sure there is a break if you have infinite loop!
        print(msg)
        response = input("==> ").strip().lower()
        if response in functions.keys():
            functions[response]()
        else:
            print('please type "s", "p", or "x"')


def print_thank_you(donor):
    print("Writing this thank you to disk: ")
    letter = "Dear {},\nThank you for your gift of ${:02.2f} to the Fund for Unmatched Socks. \nYour help will be greatly appreciated by all those who partake in our holey work.".format(donor, donors[donor][-1])
    print(letter)
    print()
    file_name = donor.replace(" ", "_") + ".txt"
    with open(file_name, "w") as output_text:
        output_text.writelines(letter)


def total_donation_amount(donor_row):
    return float(donor_row[1])


def write_all_thank_yous():
    print("Now we will write a thank you note for each donor.")
    for donor in donors:
        print_thank_you(donor)


functions = {"x": end_program,
             "p": print_report,
             "s": send_thanks,
             "w": write_all_thank_yous
             }


if __name__ == "__main__":
    main()
