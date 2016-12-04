#!/usr/bin/env python
"""Oct 23, 2016 Files lab."""

import pathlib
path = pathlib.Path('./')
for f in path.iterdir():
    print(f.absolute())

lang_dict = {}
all_lang = []
langlist = []

f = open('/Users/Mandava/Documents/python/Class2_20161004/IntroPython2016/Examples/Session01/students.txt')
f.readline()
for line in f:
    langlist = line.strip().split(':')[1]  # string
    langlist = langlist.lstrip()
    langlist = langlist.split(',')    # List
    # print(langlist)
    for item in langlist:
        if (item != ""):
            all_lang.append(item)
# print(all_lang)
for lang in all_lang:
    lang_dict[lang] = all_lang.count(lang)
# print("Language{key}: Count{value}"\.format(key=lang_dict.keys(), value=lang_dict.values()))
print(lang_dict)
print(lang_dict.keys())
f.close()

#text_src = "/Users/Mandava/Documents/python/Class2_20161004/IntroPython2016/Examples/Session01/students.txt"
image_src = "/Users/Mandava/Documents/python/Class2_20161004/IntroPython2016/students/smandava/session4/logo.jpg"
chunk_size = (512)
text_dst = open('/Users/Mandava/Documents/logo.jpg', 'wb')
f = open(image_src, 'rb')
while True:
    b = f.read(chunk_size)
    if (b != b''):
        text_dst.write(b)
        continue
    else:
        break
print('File transfer complete')
text_dst.close()
f.close()
