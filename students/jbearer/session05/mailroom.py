#!/usr/bin/env python3
"""
Excercise --  Mailroom - Session 5
October 27, 2016

Assignment: Add Exception handling and list comprehensions to mailroom.py
"""

donor_list = {'Shrek':[5,10], 'Donkey':[23,101,4], 'Princess Fiona':[7,28],
'Puss in Boots':[36,12,10], 'Gingerbread Man':[12,34]}

def print_report():
    print('{:^33}'.format('### Donor Report ###'))
    print('{:25} {:10} {:10}'.format('Name','Total','Donations'))
    
    sort_l = [(name, sum(donations), len(donations)) for (name, donations) in donor_list.items()]
    sort_l = sorted(sort_l, key=lambda donations: donations[1], reverse=True)
    sort_l = [print('{:20} {:10} {:10}'.format(i[0],i[1],i[2])) for i in sort_l]
    
def proc_donation(d_name):
    amt = True
    while amt == True:
        try:
            donation = int(input('Enter donation amount: '))
        except ValueError:
            continue
        else:
            if d_name in donor_list:
                donor_list[d_name].append(donation)
            elif d_name not in donor_list:
                donor_list[d_name] = [donation]
            print()
            print('Thank you {} for your donation of ${}!!!'.format(d_name,donation))
            print()
            amt = False
    return

def send_thanks():
    chk = True
    while chk == True:
        name = input('Enter name or type "list": ')
        if name == 'list':
            name = [print(d_names) for d_names in donor_list.keys()]
        elif name in donor_list or name not in donor_list:
            proc_donation(name)
            chk = False

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
        try:
            response = input("==> ").strip()
            if response == 'p':
                print_report()
            elif response == 's':
                send_thanks()
            elif response == 'x':
                break  # strip() in case there are any spaces
            else:
                print('please type "s", "p", or "x"')        
        except (KeyboardInterrupt, EOFError) as the_error:
            continue

if __name__ == "__main__":
    main()