#!/usr/bin/env python

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

