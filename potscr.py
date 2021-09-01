#! python

from sys import argv
import sys

ver = "0.9" # format: major potscr release number (dot) commit number
using_py = False
s_e_c_ok = False
len = 0
curnum = 0
lookinfortxt = False
txtfound = ""
stored = ""
helptxt = f"""

potatoscript parser v{ver}    

usage: potscr [-h] (input file) [-l (log file)]

arguments:

-h,--help: shows help
-l,--logpath (log file): sets a path for the log file
    
    """
noargtxt = f"""

potatoscript parser v{ver}

for help, type 'potscr --help' or 'potscr -h'
            
            """


if argv[0] == "potscr" or argv[0] == "potscr.py":
    using_py = True

if using_py:
    try:
        argv[1]
    except:
        print(noargtxt)
else:
    try:
        argv[0]
    except:
        print(noargtxt)

if using_py:
    if argv[1] == "--help" or argv[1] == "-h":
        print(helptxt)
else:
    if argv[0] == "--help" or argv[0] == "-h":
        print(helptxt)

if using_py:
    if argv[1].endswith(".potscr") or argv[1].endswith(".potato") or argv[1].endswith(".pscr"):
        file = open(argv[1],"r")
        readit = file.read()
        if not readit.startswith("~"):
            print("ERROR: This is not a PotatoScript file! Did you forget the @* in the beginning?")
        else:
            if not readit.endswith("~"):
                print("ERROR: This file has no ending command")
            else:
                s_e_c_ok = True
else:
    if argv[0].endswith(".potscr") or argv[0].endswith(".potato") or argv[0].endswith(".pscr"):
        file = open(argv[0],"r")
        readit = file.read()
        if not readit.startswith("~"):
            print("ERROR: This is not a PotatoScript file! Did you forget the ~ in the beginning?")
        else:
            if not readit.endswith("~"):
                print("ERROR: This file has no ending command")
            else:
                s_e_c_ok = True

if not s_e_c_ok:
    exit()

for c in readit:
    len += 1

for i in range(0,len):
    if readit[curnum] == "-":
        lookinfortxt = True
    elif readit[curnum] == "_":
        lookinfortxt = False
        print(txtfound[1:])
        txtfound = ""
    elif readit[curnum] == "#":
        stored = input()
    elif readit[curnum] == "$":
        print(stored,end="")
    elif readit[curnum] == "/":
        print("\n")
    
    if lookinfortxt:
        txtfound += readit[curnum]
    

    curnum += 1
