#!/usr/local/bin/python3

# Author: Darryl Wong (darrylsw@gmail.com)
# Date: 10/16/2016

#Goal:
#You work in the mail room at a local charity. Part of your job is to write 
# incredibly boring, repetitive emails thanking your donors for their generous 
# gifts. You are tired of doing this over an over again, so yo’ve decided to 
# let Python help you out of a jam.

# The program
# Write a small command-line script called mailroom.py. This script should be 
# executable. The script should accomplish the following goals:
#
# - It should have a data structure that holds a list of your donors and a 
#   history of the amounts they have donated. This structure should be 
#   populated at first with at least five donors, with between 1 and 3 
#   donations each
# - The script should prompt the user (you) to choose from a menu of 2 actions: #   ‘Send a Thank You’ or ‘Create a Report’.

# Sending a Thank You
# - If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
# - If the user types ‘list’, show them a list of the donor names and re-prompt
# - If the user types a name not in the list, add that name to the data 
#   structure and use it.
# - If the user types a name in the list, use it.
# - Once a name has been selected, prompt for a donation amount.
# - Verify that the amount is in fact a number, and re-prompt if it isn’t.
# - Once an amount has been given, add that amount to the donation history of 
#   the selected user.
# - Finally, use string formatting to compose an email thanking the donor for 
#   their generous donation. Print the email to the terminal and return to the 
#   original prompt.
#
# It is fine to forget new donors once the script quits running.
# 
# Creating a Report
# - If the user (you) selected ‘Create a Report’ Print a list of your donors, 
#   sorted by total historical donation amount.
# - Include Donor Name, total donated, number of donations and average donation #   amount as values in each row.
# - Using string formatting, format the output rows as nicely as possible. The 
#   end result should be tabular (values in each column should align with those #   above and below)
# - After printing this report, return to the original prompt.
# - At any point, the user should be able to quit their current task and return #   to the original prompt.
# - From the original prompt, the user should be able to quit the script cleanly

# data structure of donors is a list with elements that contain another list. The first element in that nested
# list is the name of the donor, and the other elements of that nested list is their donations
# example: 
#       donor_list = [["Bill Gates", 5000, 10000, 15000], ["Jeff Bezos", 1000, 2000, 3000]]

# there will be other temporary lists used to list just donors and for sorting purposes.

def main_menu():
	""" The main menu where everything starts"""
	print ("Main Menu")
	print ("1. Send a Thank You")
	print ("2. Create a Report")
	print ("3. Exit")
	return int(input ("Selection: "))

def send_thank_you(list):
	amount = input ("Enter amount: ")
	#todo - check amount is an integer
	if current_donor(list, name):
		list = add_donation(list, name, amount)
	else:
		list = add_donor(list, name, amount)
		print (list)
		print_thank_you_letter(name, amount)
	return list

def print_donors (list):
	""" Given a donor list it prints just the donors """
	print ("")
	for donations in list:
		print (donations[0])
	print ("")

def current_donor (list, donor):
	""" has this donor donated in the past? """
	for donations in list:
		if (donor == donations[0]):
			return True
	return False

def add_donation (list, donor, amount):
	""" this donor is an existing donor so we're just adding the amount to the end of his donations """
	""" we'll create a new list and just copy elements to new list until we get to our donor and then """
	""" we will modify his donation list """
	new_list = []
	for donations in list:
		if donor == donations[0]:
			donations = donations + [int(amount)]
		new_list.append (donations)
	return new_list

def add_donor (list, donor, amount):
	""" this donor doesn't exist so we'll just add him/her as an element with their donation """
	#return list + [[donor, amount]]
	list.append([donor, int(amount)])
	return list

def print_thank_you_letter (donor, amount):
	print (donor + "," + "\n")
	print ("Thank you for your donation in the amount of $" + amount + ".")
	print ("Your donation will help our organization in so many ways.")
	print ("")

def donor_totals_old (list):
	""" return an associated array with donation totals for a donor, which is the key for the array """
	new_list = {}
	for donations in list:
		donor = donations[0]
		donation_total=0
		for i in range(1,len(donations)):
			donation_total = donation_total + donations[i]
		new_list[donor] = donation_total
	#return new_list
	return sorted(new_list, key=lambda donors: donors[1])

def total_donation_sort(list):
	""" sort by total donation """
	return list[1]

def num_donation_sort(list):
	""" sort by number of donations """
	return list[2]

def avg_donation_sort(list):
	""" sort by average donation """
	return list[3]

def donor_totals (list):
	""" return a tuple with the following                   """
	""" - donor                                             """
	""" - donation total for that donor                     """
	""" - number of donations for that donor                """
	""" - average donation for that donor                   """
	new_list = []
	for donations in list:
		donor = donations[0]
		donation_total=0
		for i in range(1,len(donations)):
			donation_total = donation_total + donations[i]
		new_list.append((donor, donation_total, len(donations)-1, donation_total/(len(donations)-1)))
	return new_list

def print_report(list):
	""" print formatted report """
	print ('\n{0:<25} {1:<9} {2:<20} {3:<21}'.format ("Donor", "Total", "No. of donations", "Average donation"))
	for donation in list:
		print ('{0:<25} ${1:<8,.0f} {2:<20d} ${3:<20,.0f}'.format (donation[0], donation[1], donation[2], donation[3]))
	print ("")



if __name__ == '__main__':
	donor_list = [["Bill Gates", 5000, 10000, 15000], ["Jeff Bezos", 1000, 2000, 3000]]
	
	# let's get this puppy started
	main_input = int(0)
	while ((main_input < 1) or (main_input > 3)):
		main_input = main_menu()
		if main_input == 1:
			name = input ("Enter name or list to list donors: ")
			if name == "list":
				print_donors (donor_list)
			else:
				donor_list = send_thank_you(donor_list)
			main_input=int(0)
		elif main_input == 2:
			# create a sorted detailed donor report and print it
			print_report (sorted (donor_totals(donor_list), key=total_donation_sort, reverse=True))
			main_input=int(0)




