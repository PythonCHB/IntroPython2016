#return a sequence with the first and last items exchanged.

s = [1,2,3,4,5,6,7,8,9,10]

new=s[9:] - s[1:8] + s[0:1]
print(new)

#return a sequence with every other item removed
s = [1,2,3,4,5,6,7,8,9,10]

new= s[0:9:2]

print (new)

#return a sequence with the first and last 4 items removed, and every other item in between

s = [1,2,3,4,5,6,7,8,9,10]

new= s [1:-4:2]

print(new)


#return a sequence reversed (just with slicing)


s = [1,2,3,4,5,6,7,8,9,10]

new = s[::-1]

print(new)





