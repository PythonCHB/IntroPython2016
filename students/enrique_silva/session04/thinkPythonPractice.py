
#create a dictionary the values in "word.txt" as the keys.
new_dict=dict()

with open('words.txt','r') as words:

	for line in words:
		line= line.rstrip()
		new_dict[line]=()

print(new_dict)




#write a histogram function using the get() method, print the keys with values and sort them.

def histogram(s):
    d = dict()
    for c in s:
    	d[c] = d.get(c, 0) + 1

    return d


def print_hist(h):
	for c in sorted(h.keys()):
		print (c,h[c])

h=histogram('brontosurus')
print_hist(h)


#function that takes a value and returns the first key that maps to that value

def histogram(s):
    d = dict()
    for c in s:
    	d[c] = d.get(c, 0) + 1

    return d

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError('The value is not in the dictionary')

h=histogram('brontosurus')

k=reverse_lookup(h,2)

print(k)


#function that takes a value and returns the first key that maps to that value

def histogram(s):
    d = dict()
    for c in s:
    	d[c] = d.get(c, 0) + 1

    return d

def reverse_lookup(d, v):
	new_list=[]
    for k in d:
        if d[k] == v:
            new_list.append(k)

    return new_list


h=histogram('brontosurus')

new_list=reverse_lookup(h,3)

print(new_list)

# #Write a function called sed that takes as arguments a pattern string, a replacement string,
# and two filenames; it should read the first file and write the contents into the second file
# (creating it if necessary). If the
# pattern string appears anywhere in the file, it should be replaced with the replacement string.

import sys
def sed(pattern, replacement, input_file, output_file):
    """ reads a source file and writes the destinations file. Each line is replaced
    with replace"""

    try:
        infile=open(input_file, 'r')
        outfile=open(output_file, 'w')
        for line in infile:
            line = line.replace(pattern, replacement)
            outfile.write(line)
        infile.close()
        outfile.close()
    except:
        print("There is an error")

def main():
    pattern='bullshit'
    replacement='not nice to say'
    input_file='input.txt'
    output_file='output.txt'
    sed(pattern, replacement, input_file, output_file)

if __name__ == '__main__':
    main()


#working with databases






