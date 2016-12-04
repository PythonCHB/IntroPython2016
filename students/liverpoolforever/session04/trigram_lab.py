''' Trigram Lab - http://uwpce-pythoncert.github.io/IntroToPython/exercises/kata_fourteen.html'''

import os
from collections import defaultdict

FILE_NAME = "sherlock_small.txt"
WD = os.getcwd()
# Set than a list to avoid duplicate words?
list_words = []
# create a dict with 2 words as a key and 3rd word as value for all the words
trigram_dict = defaultdict(list)

# wrapper function for handling exceptions in inputs
def safe_input():
	try:
		response = input("==> ").rstrip()
		return response
	except (EOFError,KeyboardInterrupt) as e:
		
		print("Input interrupted by user or end of line reached")
		return None

def read_contents():
	# print(WD,FILE_NAME)
	infile_path = os.path.join(WD,FILE_NAME)
	try:
		with open(infile_path) as file_hanlder:
			# use enumerate to print line no
			for line_no,line in enumerate(file_hanlder):
				# clean up the line - 1. how to do multiple replace?   USE 'translate'
				line = line.rstrip().replace('--',' ').replace('-',' ').replace(',','').replace(',','').replace('.','').replace(')','').replace('(','')
				# split on whitespace to get all words
				list_line = line.split()
				for word in list_line:
					# get rid of blank words
					if word:
						list_words.append(word)
	except (OSError, IOError) as e:
		print(e)

def create_trigram():

	# iterate over length -2 as index+1 and index+2 will throw out of bounds for last elem
	# for same 'keys' -- comnine the value of that key as a list
	for index in range(len(list_words)-2):
		list_key = [list_words[index],list_words[index + 1]]
		key = ' '.join(list_key)
		# key = list_words[index] + ' ' + list_words[index + 1]
		value = list_words[index + 2] 
		# if key in trigram_dict.keys():
		trigram_dict[key].append(value)
		# else:
			# trigram_dict[key].append(value)
	# print(trigram_dict)


def create_text():
	#  Ask for first 2 words from the user to start
	response = safe_input()
	# Print the first word from the input
	print(response.split()[0],end = ' ')
	while True: 
		if response in trigram_dict.keys():
			# print(response, end= ' ')
			# Values of the key
			second_word = trigram_dict[response]
			# 2nd word of the user input which is the first word in the next key
			first_word = response.split()[1]
			# new_text = first_word + ' ' + str(second_word)
			# new_text = second_word
			# print(first_word,second_word)
			second_word.append(first_word)
			new_text_list = second_word[::-1]
			new_text = ' '.join(new_text_list)
			response = new_text
			print(first_word, end= ' ')
		else:
			print("Please select 2 different words to start")
			break

def main():
	#  parse the input file
	read_contents()
	# create a trigram from input file
	create_trigram()
	# create the text 
	create_text()

if __name__ == '__main__':
	main()
		   