''' File Lab 
Write a little script that reads that file, and generates a list of all the languages that have been used.
Extra credit: keep track of how many students specified each language.
'''

import os
from collections import defaultdict

NAME_OF_DIR = '/Users/nachiketgalande/Documents/UWPython/IntroPython2016/Examples/Session01'
# normal dict doesn't work for the counts - if the key is not there
lang_count = {}
# lang_count = defaultdict(int) 

def main():
	working_dir = os.getcwd()
	# print(working_dir)
	list_files(NAME_OF_DIR)


def list_files(dir_name):
	list_files = os.listdir(dir_name)
	input_file = list_files[2];
	#  Join the base path with the file name
	input_path = os.path.join(dir_name,input_file)
	# pass to iterator and counting fun
	file_iterate(input_path)

def file_iterate(file_name):

	#  use 'with' to open files

	file_hanlder = open(file_name,'r')
	for line in file_hanlder:
		# Split on comma to get students and langs
		student_list = line.rstrip('\n').split(':')
		# ignore lines without colon
		if len(student_list) > 1:
			#  split on comma to get languages
			languages = student_list[1].split(',')
			for lang in languages:
				# strip() removes whitespace at the start and end not in between
				lang = lang.strip().capitalize()
				# can do this with default dict
				if lang in lang_count.keys():
					lang_count[lang] += 1
				else:
					lang_count[lang] = 1

		else:
			print("Bad entry in file" , student_list)

	#  sort them - use a key for custom sort 
	for k,v in sorted(lang_count.items(),):
		print(k,v)

	
if __name__ == '__main__':
	main()