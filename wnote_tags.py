#!/usr/bin/env python

'''count tags in all notes and display statistics. No any kind of warranty.
	(C) D. Djokic, 2014'''

import string
import os

path = '/Users/Deki/Documents/BassDrillDelta/12-Notes'
# notes folder - hard-coded: match your path and your operating system(Windows: \\)
os.chdir(path)
files = os.listdir(path)

counts = dict()
for file in files:
    with open (file, "r") as fn:
        line = fn.readline()
        line = line.translate(None, string.punctuation)
        line = line.lower()
        tags = line.split()

        for tag in tags:
            if tag not in counts:
                counts [tag]=1
        else:
            counts [tag] +=1
    #fn.close()

tag_list = list()

for key, val in counts.items():
    tag_list.append((val, key))

tag_list.sort(reverse = True)

for key, val in tag_list : 
	print key, val
    


        
    
    
