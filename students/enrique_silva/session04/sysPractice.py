# # import sys

# import sys
# print ('this is the name of the script: ', sys.argv[0])

# print ('Number of arguments: ', len(sys.argv))

# print ('The arguments are:', str(sys.argv))



import sys

print(sys.argv)

source, dest = sys.argv[1:3]

# # binary mode important here.
# with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
#     outfile.write(infile.read())

# what if the file it too big to easily fit in memory?
# do it in chunks:

CHUNKSIZE = 128  # Really should be bigger -- 1MB? but for testing...
with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
    while True:
        data = infile.read(CHUNKSIZE)
        if not data:  # End of file
            break
        outfile.write(data)


