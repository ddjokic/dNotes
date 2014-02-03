#!usr/bin/env python

import os
import subprocess

'''Listing all tags in all wnotes and record pairs in "001-note-tag.txt" file
   No any kind of warranty!
   (c) D. Djokic, 2014'''

#hard-coded path to wnotes - change to match system (Win '\\') and real path

path = '/Users/Deki/Documents/BassDrillDelta/12-Notes'
os.chdir(path)
files1 = os.listdir(path)

files = [fi for fi in files1 if fi.endswith(".txt") or fi.endswith(".md")]

pairs = dict()  #empty dictionary to record pairs
tlist = []

for file in files:
    with open(file, "r") as fn:
        tag = fn.readline()
    pairs[file] = tag

for key, value in pairs.items():
    tlist.append((key, value))

count = len(tlist)
print (count)

recordfile = "001-note-tag.txt"
fname = open(recordfile, "w")
for i in range(0, count):
    fname.write("\n")
    fname.write (str(tlist[i]))
fname.close()

if os.sys.platform.startswith('darwin'):
    subprocess.call(('open', recordfile))
elif os.name == 'nt':
    os.startfile(recordfile)
elif os.name == 'posix':
    subprocess.call(('xdg-open', recordfile))
