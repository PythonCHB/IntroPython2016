#!/usr/bin/env python3
"""
Excercise --  Test mailroom.py definitions with pytest
November 2, 2016
"""

donor_list = {'Shrek':[5,10], 'Donkey':[23,101,4], 'Princess Fiona':[7,28],
'Puss in Boots':[36,12,10], 'Gingerbread Man':[12,34]}

sort_list = []

def print_report(sort_list):
    print('{:^33}'.format('### Donor Report ###'))
    print('{:25} {:10} {:10}'.format('Name','Total','Donations'))
    [print('{:20} {:10} {:10}'.format(i[0],i[1],i[2])) for i in sort_list]

def sort_donors(): 
    global sort_list
    sort_list = [(name, sum(donations), len(donations)) for (name, donations) in donor_list.items()]
    sort_list = sorted(sort_list, key=lambda donations: donations[1], reverse=True)
    
def get_donation(d_name):
    amt = True
    while amt == True:
        try:
            donation = int(input('Enter donation amount: '))
        except ValueError:
            continue
        else:
            amt = False
            proc_donation(d_name, donation)
            print_donation(d_name, donation)

def proc_donation(d_name, donation):
    if d_name in donor_list:
        donor_list[d_name].append(donation)
    elif d_name not in donor_list:
        donor_list[d_name] = [donation]

def print_donation(d_name, donation):
    print()
    print('Thank you {} for your donation of ${}!!!'.format(d_name,donation))
    print()

def send_thanks():
    chk = True
    while chk == True:
        d_name = input('Enter name or type "list": ')
        if d_name == 'list':
            d_name = [print(d_names) for d_names in donor_list.keys()]
        elif d_name in donor_list or d_name not in donor_list:
            get_donation(d_name)
            chk = False

msg = """
What would you like to do?
To send a thank you: type "s"
To print a report: type "p"
To exit: type "x"
"""

def main():
    response = ''
    while True:
        print(msg)
        try:
            response = input("==> ").strip()
            if response == 'p':
                sort_donors()
                print_report(sort_list)
            elif response == 's':
                send_thanks()
            elif response == 'x':
                break
            else:
                print('please type "s", "p", or "x"')        
        except (KeyboardInterrupt, EOFError) as the_error:
            continue

if __name__ == "__main__":
    main()