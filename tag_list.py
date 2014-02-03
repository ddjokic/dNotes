#!/usr/bin/env python

import os
import string
import subprocess

# hard coded path - change to match operating system and real path
path = '/Users/Deki/Documents/BassDrillDelta/12-Notes'
os.chdir(path)
files1 = os.listdir(path)
files = [fi for fi in files1 if fi.endswith(".txt") or fi.endswith(".md")]

tag_list=[]
duplicates = []
for file in files:
    with open(file, "r") as fn:
        line = fn.readline()
        line = line.translate(None, string.punctuation)
        line = line.lower() 
        tags = line.split()
        for tag in tags:
            if tag not in tag_list:
                tag_list.append(tag)
            else:
                duplicates.append(tag)
count1=len(tag_list)
count2=len(duplicates)

print(count1)
recordfile = "002-tags-list.txt"
fname = open(recordfile, "w")
for i in range(0, count1):
    fname.write("\n")
    fname.write (str(tag_list[i]))
fname.close()
        
if os.sys.platform.startswith('darwin'):
    subprocess.call(('open', recordfile))
elif os.name == 'nt':
    os.startfile(recordfile)
elif os.name == 'posix':
    subprocess.call(('xdg-open', recordfile))  
