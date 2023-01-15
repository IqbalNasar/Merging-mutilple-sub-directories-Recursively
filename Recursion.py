mport os

import pathlib
from pathlib import Path

import glob
import shutil
directory = "new_directory"
parant_directory =os.path.join (r"C:\Users\Nasir\PycharmProjects\")
make_directory = directory
os.mkdir(make_directory)   
new_directory=make_directory

def move(shift):
   for images in glob.iglob(f'{shift}/*'):

        if (images.endswith(".png")):
            shutil.move(images, new_directory)

def Recurseion(Record):
    curr = len(Record) - 1
    print('the curr is:',curr)
    current = Record[curr]
    print('The main direectory is:', current)
    filelist = pathlib.Path(current)
    filelist = os.listdir(current)
    print('The filelist is: ', filelist)


    lps = len(filelist)
    i=0
    while i<lps:
        sub = os.path.join(current, filelist[i])
        sub= pathlib.Path(sub)
        print('The bc or subdirectory is  :', sub)
        a=os.listdir(sub)
        f1=a[0]
        file_name, file_extension = os.path.splitext(f1)
        if file_extension=='.png':
            move(sub)
        elif file_extension=='':
            print('Is this even repeated?')
            Record.append(sub)
            print('the new record is:',Record)
            Recurseion(Record)
        i+=1

Record=[]

dir =os.path.join(r"C:\Users\Nasir\PycharmProjects\benign\SOB")
Record.append(dir)

Recurseion(Record)
