#!/usr/bin/env python3

# === File Lab =====

'''
write a program which prints the full path to all files in the current 
directory, one per line
'''

import os

print('\nFull path to current directory:')
print(os.getcwd())

# create list of all files in current directory
directory_list = os.listdir()

print('\nFiles in current directory:')
for entry in directory_list:
    print("\t", entry)

print('\n'*2)
print('-'*80)
print('\n'*2)

'''
Write a program which copies a file from a source, to a destination (without 
using shutil, or the OS copy command)
'''

# Function to create 80 character line of gibberish
def line_of_gibberish():
    import random
    line = ""
    for i in range(80):
        line = line + chr(random.randint(41,79)) #$Todo: hex
    line = line + "\n"
    return line

# Create file to use as source
file_object = open('source_file.txt', 'w')
for i in range(100):
    file_object.write(line_of_gibberish())
file_object.close()

# Copy source to target line by line
target_file_object = open('target_file.txt','w')
source_file_object = open('source_file.txt','r')
while True:
    line = source_file_object.readline()
    if not line:
        break
    else:
        target_file_object.write(line)
target_file_object.close()
source_file_object.close()

'''
Write a little script that reads that file (students.txt), and generates a
list of all the languages that have been used.

Extra credit: keep track of how many students specified each language.
'''

# Create a dictionary from students.txt file
# key = name, value = languages
students_dictionary = {}

for line in open('../../../Examples/Session01/students.txt'):
    student_info = []
    student_info = line.split(':')
    if len(student_info) == 2:
        students_dictionary[student_info[0]] = student_info[1].replace('\n', ' ')
    else:
        students_dictionary[student_info[0]] = '<n/a>'

# Get rid of 'name: languages' header line
students_dictionary.pop('name')

# Create a dictionary of languages
# key = language, value = count
# $todo value = list of students who know that language
language_dictionary = {}
language_list = students_dictionary.values()
for entry in language_list:
    entry = entry.lower().replace(',', '').replace('pyton', 'python').replace('macscript', 'maxscript')
    entry_list = entry.split()
    for language in entry_list:
        if language in language_dictionary:
            language_dictionary[language] = language_dictionary[language] + 1
        else:
            language_dictionary[language] = 1

# Print Languages & number of users            
for languages in language_dictionary:             
    print("{}\t{:10.0f}".format(languages.ljust(12), language_dictionary[languages]))

if __name__ == '__main__':
    print('\n=== MAIN ===\n')
    
'''
=== SAMPLE ===

In [20]: run file_lab.py

Full path to current directory:
/Users/paulvosper/UWPCE_IntroPython2016/IntroPython2016/students/pvosper/session04

Files in current directory:
	 .DS_Store
	 dict_lab.py
	 file_lab.py
	 kata_14_trigrams.py
	 lorem_ipsum_generator.py
	 myfile
	 sherlock.txt
	 sherlock_partial.txt
	 source_file.txt
	 target_file.txt
	 temp_file.txt



--------------------------------------------------------------------------------



swift       	         1
asp         	         1
r           	         4
bash        	         6
cobol       	         1
ruby        	         2
sas         	         1
python      	        19
perl        	         3
c           	         2
maxscript   	         1
german      	         1
qbasic      	         1
actionscript	         1
php         	         4
xml         	         1
basic       	         2
sql         	        12
htl         	         1
html        	         7
javascript  	         1
c#          	         2
c++         	         5
scala       	         1
java        	         3
shell       	         2

=== MAIN ===

'''