#!/usr/bin/env python
'''Creates new text note, with predefined filename, insert "# Tags" as first line in the file and open it in default Text Editor. If files exist, script append existing file.
This scheme is used for my work related notes. Path to the notes  is hard-coded on line 12: change it to suit needs and OS. Windows path: C:\\Path\To\\notes.

(C) 2014, D.Djokic'''

import os
import subprocess
import datetime

# hard coded path to notes!:
path = '/Users/Deki/Documents/BassDrillDelta/12-Notes'

now=datetime.datetime.now()
ss = str(now.year)+str(now.month)+str(now.day)

print ('1 - Todox - Todo \n2 - Planx - Planning/Schedules \n3 - Engx - Engineering \n4 - Constx - Construction \n5 - Saftx - Safety \n6 - Sitx - Site Organization \n7 - Budgx - Budget \n8 - Makx - Makers \n9 - Momx - Minutes of Meeting \n10 - Repx - Reports')

num = raw_input ("Enter your choice 1-10: ")
description = raw_input ("Enter descriptive file title: ")
tag = raw_input ("Enter tags, separated by comma: ")

prefix = ['Todox', 'Planx', 'Engx', 'Constx', 'Saftx', 'Sitx', 'Budgx', 'Makx', 'Momx', 'Repx']

file_prefix = prefix [int(num)-1]

# hard coded path to notes!:
filename = file_prefix + ' - ' + ss + ' - ' + description + '.txt'

os.chdir (path)
fn=open(filename, 'a')
fn.write ('#' + tag)
fn.write ('\n')
fn.close()

if os.sys.platform.startswith('darwin'):
    subprocess.call(('open', filename))
elif os.name == 'nt':
    os.startfile(filename)
elif os.name == 'posix':
    subprocess.call(('xdg-open', filename))