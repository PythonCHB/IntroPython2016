#!/usr/bin/env python
"""Oct 23, 2016 Trigram lab."""

file_path = '/Users/Mandava/Documents/python/Class2_20161004/IntroPython2016/students/smandava/session4/'
file_src = '/Users/Mandava/Documents/python/Class2_20161004/IntroPython2016/students/smandava/session4/sherlock_small.txt'
trigram_dst = open('/Users/Mandava/Documents/python/Class2_20161004/IntroPython2016/students/smandava/session4/sherlock_small_trigram.txt', 'w')
file_dict = {}
key_list = []
tri_list = []
tri_input = []

f = open(file_src, 'r')
b = f.read()
l = b.strip().split(' ')
# print(l)
if (b != b''):
    for index in range(len(l) - 2):
        file_dict[l[index], l[index + 1]] = l[index + 2]
    # print(file_dict)
for key in file_dict.keys():
# while key in file_dict.keys():
    if (key not in file_dict.keys()):
        print('key not in the dictionary is:', key)
        file_dict.setdefault('sasi', 'mandava')
        break
    else:
        key_list = [key]
        # tri_input = key_list.append(file_dict[key])
        tri_input = key_list[0][0] + " " + key_list[0][1] + " " + file_dict[key]
        trigram_dst.write(tri_input)
        key = (key_list[0][1], file_dict[key])
        continue
print('New trigram file created.')
trigram_dst.close()
f.close()
