#!/usr/bin/env python
'''Creates new text note, with predefined filename, insert "# Tags" as first line in the file and open it in default Text Editor. If files exist, script append existing file.
This scheme is used for my private (not job-related) notes. Path to the notes  is hard-coded on line 12: change it to suit needs and OS. Windows path: C:\\Path\To\\notes

(C)2014, D.Djokic'''

import os
import subprocess
import datetime

# hard coded path to notes!:
path = '/Users/Deki/Dropbox/Notes'

now=datetime.datetime.now()
ss = str(now.year)+str(now.month)+str(now.day)

print ('1 - Citx - Citations \n2 - Prodx - Productivity \n3 - Progx - Programming \n4 - Refx - References\n5 - Jobx - Job Hunting \n6 - Bashx - Unix and Linux commands \n7 - Travx - Traveling \n8 - Docx - Important Documents\n9 - Todox - To do, planning \n10 - Idx - Idea \n11 - Thox - Thoughts \n12 - Photx - Photos \n13 - Softx - Software')

num = raw_input ("Enter your choice 1-13: ")
description = raw_input ("Enter descriptive file title: ")
tag = raw_input ("Enter tags, separated by comma: ")

prefix = ['Citx', 'Prodx', 'Progx', 'Refx', 'Jobx', 'Bashx', 'Travx', 'Docx', 'Todox', 'Idx', 'Thox', 'Photx', 'Softx']

file_prefix = prefix [int(num)-1]

# hard coded path to notes!:
filename = file_prefix + ' - ' + ss + ' - ' + description + '.txt'

os.chdir (path)
fn=open(filename, 'a')
fn.write ('#' + tag + "\n" )
fn.close()

if os.sys.platform.startswith('darwin'):
    subprocess.call(('open', filename))
elif os.name == 'nt':
    os.startfile(filename)
elif os.name == 'posix':
    subprocess.call(('xdg-open', filename))