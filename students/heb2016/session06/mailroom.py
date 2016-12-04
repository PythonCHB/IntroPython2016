
#!/usr/bin/env python


def print_report(donorlist):
    print("This will print a report")
    row=0
    while row<=len(donorlist)-1:
            print_list =donorlist[row]
            row_msg="{:s},{:d},{:d}".format(*donorlist[row])
            print(row_msg)
            row+=1
    return()



def send_thanks(donorlist):

    print("This will write a thank you note")

    def input_name():
        msg ="""
            Your Name
            """
        print(msg)
        try:
            response_name = input("==> ").strip()
         except:
             raise(response_name not in ('abcdefghi'))
             input_name()

        row =1
        in_list = False
        while (row <= len(donorlist)):
            if response_name == donorlist[row-1][0]:       
                in_list = True
                print("Name exist. Try again")
                input_name()
            row+=1

        if in_list == False:
            response = [response_name]
            row=1
            while row <= 3:
                print("Please input donation amount")
                response_donation = input("==> ").strip()
                if int(response_donation) <=0:
                    response_donation = input("reinput==> ").strip()
                
                response.append( int(response_donation))
                
                row+=1
            
            donorlist.append(response)
            print("Thank you donor: {:s},".format(*response))
                     
            return()

    input_name()
    return(donorlist)
   

# here is where triple quoted strings can be helpful
msg = """
    What would you like to do?
    To send a thank you: type "s"
    To print a report: type "p"
    To exit: type "x"
    """
donorlist = [("name1", 10,20,20), ("name2", 20,20,20),  ("name3", 10,20,20),("name4", 20,20,30),  ("name5", 40,20,20)]
print(len(donorlist))




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
            print_report(donorlist)
        elif response == 's':
            send_thanks(donorlist)
        elif response == 'x':
            break
        else:
            print('please type "s", "p", or "x"')



if __name__ == "__main__":

    main()
