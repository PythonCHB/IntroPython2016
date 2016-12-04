#!/Users/jhefner/python_dev/uw_python/bin/python
verbose = False

history = {
"Zapp Brannigan": [50, 73, 10],
"Philip J Fry": [5],
"Bender Bending Rodriguez": [500],
"Turanga Leela": [7, 20, 96],
"Hermes Conrad": [11, 14, 22],
"Amy Wong": [8, 27, 34],
}

def check_if_donor(thank_you_name):
    if thank_you_name in history:
        return True
    else:
        history[thank_you_name]=[]
        return False

def send_thank_you():
    if verbose: print("send_thank_you()")
    while True:
        print("--------------------------")
        print("--------------------------")
        print("--------------------------")
        print("Alright lets send that thank you note.")
        print("Type \"list\" if you need to be reminded of the donors.")
        print("Otherwise just type the persons full name.")
        thank_you_name = input("\n>>> ")
        if thank_you_name == "list":
            print("Here's the list of our donors:")
            for i in history: print("> ",i)
            thank_you_name = input("\n>>> ")

        check_if_donor(thank_you_name)

        print("And what was their donation amount?")
        donation_input = input("\n>>> ")
        while not donation_input.isnumeric():
            print("And what was their donation amount? (e.g. 10)")
            donation_input = input("\n>>> ")
        donation_input = int(donation_input)
        history[thank_you_name]=[int(donation_input)]
        print("\n\nDear "+thank_you_name+",\nIt is with great thanks that we send this note in reception of your donation. Please accept our gratitude and think of us again in the future.\nSincerely,\n\tUs\n\n")
        break
    return True

def create_a_report(history):
    if verbose: print("create_a_report()")
    report_rows = []
    for key, value in history.items():
        total_gifts = sum(value)
        num_gifts = len(value)
        avg_gift = total_gifts / num_gifts
        report_rows.append((key,total_gifts, num_gifts, avg_gift))

    print("{:25s} | {:11s} | {:9s} | {:12s}".format(
        "Donor Name", "Total Given", "Num Gifts", "Avg Gift"))
    print("-"*66)
    for row in report_rows:
        print("{:25s}   {:11.2f}   {:9d}   {:12.2f}".format(*row))
    return True

def main():
    if verbose: print("main()")
    while True:
        main_menu_choice=0
        print("--------------------------")
        print("What would you like to do?")
        print("--------------------------\n")
        print("Enter the # for your selection")
        print("1. Send a Thank You\n2. Create a Report\n3. Exit")
        main_menu_choice = input("\n>>> ")
        if main_menu_choice == "1":
            send_thank_you()
        elif main_menu_choice == "2":
            create_a_report(history)
        elif main_menu_choice == "3":
            break
        else:
            print("\n\n\nPlease try your selection again.")


if __name__ == '__main__':
    main()