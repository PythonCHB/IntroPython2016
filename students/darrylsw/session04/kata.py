#!/usr/local/bin/python3

# Author: Darryl Wong (darrylsw@gmail.com)
# Date: 10/23/2016

# Trigrams
# Trigrams can be used to mutate text into new, surreal, forms. But what heuristics do we apply to get a reasonable result?

import random

def analyze_text(file):
	f = open (file)
	dict={}
	next2last = ""
	while (True):
		line=f.readline()
		if not line:
			break
		line =line.strip ('\n').split(" ")
		#print (line)
		for i in range (1, len(line)-1):
			if (next2last != ""):   # if we already read a line, let's get the information from the end of that line
				#print (next2last, last, line[0])
				key = (next2last, last)
				dict[key] = line[0]
				next2last = ""
				#print ("key: {} value: {}".format (key, line[0]))
			else:
				#print (line[i-1], line[i], line[i+1])
				key = (line[i-1], line[i])
				#print (key)
				dict[key] = line[i+1]
				#print ("key: {} value: {}".format (key, line[i+1]))
		next2last = line[len(line)-2]
		last = line[len(line)-1]
	f.close()
	return dict


def seed_text (dict, first="", second=""):
	if (first == "" and second == ""):
		# randomly select first sequence
		count = len(dict)
		rand = random.randrange(1, count)
		i = 1
		for key in dict.keys():
			#print ("keys = ", key)
			if i == rand:
				initial_key = key
			i = i+1
		first = initial_key[0]
		second = initial_key[1]
		third = dict[initial_key]
	
		print ("{} {} {}".format(first, second, third), end=" ")
		return (second, third)
	else:
		key = (first, second)
		value = dict[key]
		print ("value: ", value)
		if value == None:
			seed_text (dict)
		else:
			print ("{}".format(dict[key]), end=" ")
			return (second, dict[key])
		

def generate_text (dict):
	(first, second) = seed_text(dict)
	for i in range (100):
		(first, second) = seed_text(dict, first, second)





def main():
	dict = analyze_text ("./sherlock.txt")
	#print (dict)
	#print ()
	generate_text(dict)




if __name__ == '__main__':
	main()





