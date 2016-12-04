#!/usr/bin/env python3
"""Nov 19 2016 Mail room Exercise with exceptions and comprehension in print function."""
import operator
donor_dict = {'Alfred Hitchcock': [10, 20, 30],
              'Martin Scorsese': [20, 30, 40],
              'Steven Spielberg': [40, 20, 30, 10],
              'Francis Coppola': [10, 10, 10],
              'Ridley Scott': [10, 20, 30, 10]}

donor_summary_dict = {}


def print_report():
    """Print Report."""
    print("This will print a report.")
    # donor_list_new = []
    report_header = ("{0:<30s} {1:<30s} {2:<30s} {3:<30s}".
                     format('Donor Name',
                            'Total Amount', 'No.of Donations',
                            'Avg.Donation'))

    # report_header = report_header.replace(',', '')
    print(report_header)
    for donorname in donor_dict.keys():
        donation_amounts = donor_dict[donorname]
        donation_sum = sum(donation_amounts)
        donation_avg = donation_sum / len(donation_amounts)
        donor_summary_dict[donorname] = [donation_sum, len(donation_amounts),
                                         donation_avg]
    sorted_donors = sorted(donor_summary_dict.items(),
                           key=operator.itemgetter(1), reverse=True)
    for donor in (sorted_donors):
        print('{0:<30s} {1:<30.2f} {2:<30d} {3:<30.2f}'.
              format(donor[0], donor[1][0], donor[1][1], donor[1][2]))


def send_thanks():
    """Send thanks to donors."""
    print("This will write a thank you note")
    print("Enter the word 'list' to see list of donors or \
          enter donor name followed by amount.")
    user_input = input("Enter the word 'list' or donor's full name:")
    if (user_input == 'list'):
        print("List of Donors:", donor_dict)
        user_input = input("Enter full name of donor:")
    if user_input in donor_dict.keys():
        try:
            d_amount = int(input("Please enter the donation amount:"))
        except ValueError:
            d_amount = int(input("Please enter only numbers for donation amount:"))
        donor_dict.setdefault(user_input, []).append(d_amount)
        print('''Dear {name}, Thank you very much for your generous \
              donation of ${amount}'''
              .format(name=user_input, amount=d_amount))
    else:
        try:
            d_amount = int(input("Please enter the donation amount:"))
        except ValueError:
            d_amount = int(input("Please enter only numbers for donation amount:"))
        donor_dict.setdefault(user_input, []).append(d_amount)
        print("Adding new donor.")
        print('''Dear {name}, Thank you very much for your generous donation of ${amount}'''
              .format(name=user_input, amount=d_amount))


def write_letter():
    """Writing a individual thank you letter to disk."""
    for donor in donor_dict.keys():
        with open('/Users/Mandava/Documents/python/Class2_20161004/IntroPython2016/students/smandava/session4/thankyouletter_{}.txt'.format(donor), 'w') as thankyou_file:
            # thankyou_file = open('/Users/Mandava/Documents/python/Class2_20161004/IntroPython2016/students/smandava/session4/thankyouletter_{}.txt'.format(donor), 'w')
            thankyou_note = ('''Dear {donor}, \n \n Thank you very much for your generous donation of ${amount}.
                                \n \n Regards, \n Seattle Charity Org \n'''
                             .format(donor=donor, amount=donor_dict[donor]))
            thankyou_file.write(thankyou_note)
    print("Created Thank you letter!")
    # thankyou_file.close()


# here is where triple quoted strings can be helpful
msg = """
What would you like to do?
To send a thank you: type "s"
To print a report: type "p"
To write a thank you letter to disk: type "w"
To exit: type "x"
"""


def main():
    """Run the main interactive loop."""
    response = ''
    select = {'p': print_report, 's': send_thanks, 'w': write_letter,
              'x': 'break'}
    # keep asking until the users responds with an 'x'
    while True:
        print(msg)
        response = input("==> ").strip()  # strip()in case there are any spaces
        if response == 'p':
            select['p']()
        elif response == 's':
            select['s']()
        elif response == 'w':
            select['w']()
        elif response == 'x':
            break
        else:
            print('please type "s", "p", or "x"')

if __name__ == "__main__":
    main()
