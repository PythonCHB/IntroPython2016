#!/usr/bin/env python

# User prompt at the beggining of program, asking what the user would like to do.

donor_list=[['enrique silva',[100, 200, 300]],
['jon smith',[200, 300, 400]],
['ally smith',[200, 300, 500]],
['anny gill', [300, 600, 1500]],
['terry bill', [500, 750, 1000]]]

msg = """
What would you like to do?

To send a thank you: type "s"
To print a report: type "p"
To exit: type "x"
"""

def main(donor_list):
    """run the main interactive loop"""

    response = ''
    # keep asking until the users responds with an 'x'
    while True:  # make sure there is a break if you have infinite loop!
        print(msg)
        response = input("==> ").strip()  # strip() in case there are any spaces

        if response == 'p':
            print_report(donor_list)
        elif response == 's':
            send_thanks(donor_list)
        elif response == 'x':
            break
        else:
            print('please type "s", "p", or "x"')

def send_thanks(donor_list):
    """Send a thank you note to donor, add the donor to the list, or  accept
    a new donation"""
    user_name=str(input("""Type "list" to see donors in database or  enter first name and last name: """))
    #TODO need to add validation on input from the user. need both to validate entries other than name or list and also account for capitalization of names and whitespace/
    print()
    if user_name== 'list':
        print_donor_list(donor_list)
    else:
        search_donor_list(donor_list,user_name)

def print_donor_list(donor_list):
    for donor in donor_list:
        print(donor[0])

def search_donor_list(donor_list, user_name):
    """search thorugh list for name entered by potential donor, if name does not exist
    add name to and ask for donation, if it does, as for donation"""
    #for user_name in donor_list[0]:
    for ind, donor in enumerate(donor_list):
        if user_name in donor:
        	existing_donor_index=ind
        	#print(existing_donor_index)--check to make sure my program is doing the right thing, REMOVE
        	#print(donor_list)
        	prompt_donation_existing(donor_list, user_name,existing_donor_index)
        	break
    else:
        donor_list.append([user_name])
        print (user_name,'added to the donor list.')
        prompt_donation_new(donor_list,user_name)
        print(donor_list)

def prompt_donation_existing(donor_list, user_name,existing_donor_index):
     """ensure donation amount is an int and add donation to list for the existing donor"""
     donation_amount= int(input('How much would you like to donate? '))
     #TO DO add exception handling on invalid input
     print()
     donor_list[existing_donor_index][1].append(donation_amount)
     send_email(donor_list, user_name,donation_amount)

def prompt_donation_new(donor_list, user_name):
     """ensure donation amount is an int and add donation to list for the new donor"""
     donation_amount= int(input('How much would you like to donate? '))
     #TO DO add exception handling on invalid input
     print()
     donor_list[-1].append([donation_amount])
     send_email(donor_list, user_name,donation_amount)

def send_email(donor_list, user_name, donation_amount):
    """write and send email to donor, thanking them for donation"""
    print('Hello {},\n\nThank you for generous danation of {:d}.\n\nSincerely, THE STAFF'.format(user_name,donation_amount))


def print_report(donor_list):
    """print a report, that lists donor, total given, number of gifts, and average donation amounts"""
    report_entries=[]
    for (donor,donations) in donor_list:
        total_donations = sum(donations)
        count_gifts = len(donations)
        avg_donation = total_donations / count_gifts
        report_entries.append((donor, total_donations, count_gifts,avg_donation))

    print("{:25s} | {:11s} | {:9s} | {:12s}".format(
          "Donor Name", "Total Donated", "Num Gifts", "Average Gift"))
    print("-" * 66)
    for row in report_entries:
        print("{:25s}   {:11.2f}   {:9d}   {:12.2f}".format(*row))

main(donor_list)

