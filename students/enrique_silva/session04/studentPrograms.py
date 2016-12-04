# You will find the list I generated in the first class of all the students in the class,
# and what programming languages they have used in the past.
# Write a little script that reads that file, and generates a list of all the languages
# that have been used. Extra credit: keep track of how many students specified each language.

import sys

print (sys.argv)

infile, outfile = sys.argv[1], sys.argv[2]

unique_languages=set()

with open(infile) as inf, open(outfile, 'w') as outf:
	inf.readline()
	for line in inf:
		langs=line.partition(':')[2]
		langs=langs.replace(',','').replace('and','')
		langs=langs.split()
		for lang in langs:
			lang=lang.strip().upper()
			unique_languages.add(lang)

for lang in unique_languages:
	print(lang)






