''' Dictionary Lab '''

inputDict = {'name':'Chris','city':'Seattle','cake':'Chocolate'}

def print_dict(dict):
    for key,value in dict.items():
        print(key,value)

def delete_item(key):
    # specificy the key to delete
    del inputDict[key]
    print(inputDict)

def add_an_item(key,value):
    inputDict[key] = value
    print(inputDict)

def display_keys(dict):
    list_of_keys = dict.keys()
    print(list_of_keys)

def display_values(dict):
    list_of_values = dict.items()
    print(list_of_values)

def check_key_exists(key):
    # call display keys
    # list_of_keys = list(dict.keys())
    if key in inputDict:
        print("{:s} exists in dictonary".format(key))

def new_dict(dict):
    # list_of_values = dict.items())
    count_dict = {}
    counter = 0;
    for key,value in dict.items():
        # count_list.append(value)
        for char in value:
            if char == 't':
                counter =+ counter + 1
            count_dict[key] = counter
    print(count_dict)

def main():
    # iterate key, value pairs
    print_dict(inputDict)
    # display keys
    display_keys(inputDict)
    # display values
    display_values(inputDict)
    # remove a key
    delete_item('cake')
    # add a ket
    add_an_item('fruit','Mango')
    # check if fruit exists
    check_key_exists('fruit')
    # new dict
    new_dict(inputDict)


if __name__ == '__main__':
    main()