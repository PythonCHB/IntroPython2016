
#!usr/bin/env python

import pathlib
import os

## Print full pathdef file_path():
def file_path():
    pth=pathlib.Path('./')
    for f in pth.iterdir():
        print(pth.absolute(),'/',f) 
    
file_path()

## Copy/Paste to new destination
def file_move():
    with  open('students.txt','r') as fr:
        with open('students_cp.txt', 'w') as fw:
            fw.write(fr.read())
            fw.close()
        fr.close()
    print("The copy of file 'students.txt' exist: ", os.path.exists('students_cp.txt'))
  

file_move()
