#!/usr/bin/env python

#Declare donor list

donorList = {'Gerrard':[1,2],'Suarez':[1,2],'Klopp':[1,2],'Torres':[1,2],'Coutinho':[1,2]}

# declare questions to be asked
ASK_NAME = "Please enter your full name"
ASK_DONATION = "Please enter donation amount"

# declare email to be sent
EMAIL = "{:25s}   {:11.2f}   {:9d}   {:12.2f}"

# Sorry I copied your print_report method!
def print_report():
    # iterate over the donor list
    reportRows = []
    for donor,amt in donorList.items():
        totalAmt = sum(amt)
        numAmt = len(amt)
        avgAmt = totalAmt / numAmt
        reportRows.append((donor, totalAmt, numAmt, avgAmt))

    #print the donors
    print("-" * 66)
    for row in reportRows:
        print(EMAIL.format(*row))


def send_thanks():
    print(ASK_NAME)
    listOfDonors = list(donorList.keys())
    res = input("==> ").strip()
    # if donor types list
    if res == 'list':
        print("list of donors are : " , listOfDonors)
    elif res in listOfDonors:
        print("Donor present")
        addAmt(res)
    else:
        # Ask if you a donor
        print('Are a new donor ? , Type "y" or "n" ')
        newDonor = input("==> ").strip()
        if newDonor == 'y':
            print(ASK_NAME)
            resName = input("==> ").strip()
            #  add the new donor
            donorList[resName] = []
            #  send the donor for his amount
            addAmt(resName)
        else:
            print('please type "list",or name of donor')

# helper methods

def addAmt(nameOfDonor):
    print(ASK_DONATION)
    resAmt = input("==> ").strip()
    # convert amt to int
    resAmt = int(resAmt)
    if isinstance(resAmt,int):
        print("The amount is: " , resAmt)
        donorList[nameOfDonor].append(resAmt)
        # Write the email here
        # EMAIL.format(nameOfDonor,resAmt)
        print(EMAIL.format(nameOfDonor,resAmt))
    else:
        print("Please enter donation as a number")

# here is where triple quoted strings can be helpful
msg = """
What would you like to do?

To send a thank you: type "s"
To print a report: type "p"
To exit: type "x"
"""

# wrapper function for handling exceptions in inputs
def safe_input():
    pass

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
