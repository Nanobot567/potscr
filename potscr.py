#! python

from sys import argv
import sys
from time import sleep
import os

ver = "2.17" # format: major potscr release number (dot) commit number

using_py = False
script_ok = False
lookinfortxt = False
logit = False
len = 0
curnum = 0
txtfound = ""
stored = ""
logpath = ""
storednum = 0

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
        exit()
else:
    try:
        argv[0]
    except:
        print(noargtxt)
        exit()

if using_py:
    if argv[1] == "--help" or argv[1] == "-h":
        print(helptxt)
else:
    if argv[0] == "--help" or argv[0] == "-h":
        print(helptxt)

tempnum = -1
for i in argv:
    tempnum += 1
    print(tempnum,i)
    if i == "--logpath" or i == "-l":
        logit = True
        try:
            print(argv[tempnum+1])
            logpath = argv[tempnum+1]
            logfile = open(logpath,"x")
        except FileExistsError:
            os.remove(logpath)
            print(argv[tempnum+1])
            logpath = argv[tempnum+1]
            logfile = open(logpath,"x")

if using_py:
    if argv[1].endswith(".potscr") or argv[1].endswith(".potato") or argv[1].endswith(".pscr"):
        file = open(argv[1],"r")
        readit = file.read()
        if not readit.startswith("~"):
            print("ERROR: This is not a potatoscript file! Did you forget the ~ in the beginning?")
        else:
            if not readit.endswith("~"):
                print("ERROR: This file has no ending indicator!")
            else:
                script_ok = True
else:
    if argv[0].endswith(".potscr") or argv[0].endswith(".potato") or argv[0].endswith(".pscr"):
        file = open(argv[0],"r")
        readit = file.read()
        if not readit.startswith("~"):
            print("ERROR: This is not a potatoscript file! Did you forget the ~ in the beginning?")
        else:
            if not readit.endswith("~"):
                print("ERROR: This file has no ending indicator!")
            else:
                script_ok = True

if not script_ok:
    exit()

for c in readit:
    len += 1

for i in range(0,len):
    if readit[curnum] == "-": # start of print
        lookinfortxt = True
        if logit:
            logfile.write("LOG: print start\n")
    elif readit[curnum] == "_": # end of print
        lookinfortxt = False
        if readit[curnum+1] == "%": # percentage after means an alt version of the command, in this case no newline
            sys.stdout.write(txtfound[1:])
            sys.stdout.flush()
            if logit:
                logfile.write("LOG: print end (no newline)\n")
                logfile.write(f"LOG: printed {txtfound[1:]}\n")
                txtfound = ""
        else:
            print(txtfound[1:])
            if logit:
                logfile.write("LOG: print end\n")
                logfile.write(f"LOG: printed {txtfound[1:]}\n")
                txtfound = ""
    elif readit[curnum] == "#": # get input
        stored = input()
        if logit:
            logfile.write("LOG: got input from user\n")
            logfile.write(f"LOG: stored = {stored}\n")
    elif readit[curnum] == "$": # print stored var
        print(stored,end="")
        if logit:
            logfile.write(f"LOG: printed stored ({stored})\n")
    elif readit[curnum] == "/": # newline
        print("")
        if logit:
            logfile.write("LOG: printed newline\n")
    elif readit[curnum] == "*": # reset stored number
        storednum = 0
        if logit:
            logfile.write("LOG: storednum reset\n")
    elif readit[curnum] == "+": # number +1
        if readit[curnum+1] == "%":
            if readit[curnum+2].isnumeric():
                storednum += int(readit[curnum+2])
            else:
                storednum += 5
            if logit:
                logfile.write(f"LOG: added five to storednum (now {storednum})\n")
        else:
            storednum += 1
            if logit:
                logfile.write(f"LOG: added one to storednum (now {storednum})\n")
        
    elif readit[curnum] == "`": # number -1
        if readit[curnum+1] == "%":
            if readit[curnum+2].isnumeric():
                storednum -= int(readit[curnum+2])
            else:
                storednum -= 5
            if logit:
                logfile.write(f"LOG: subtracted five from storednum (now {storednum})\n")
        else:
            storednum -= 1
            if logit:
                logfile.write(f"LOG: subtracted one from storednum (now {storednum})\n")
    elif readit[curnum] == "^": # print stored num
        print(storednum,end="")
        if logit:
            logfile.write(f"LOG: printed storednum ({storednum})\n")
    elif readit[curnum] == "@": # sleep
        try:
            sleep(int(readit[curnum+1]))
            if logit:
                logfile.write(f"LOG: slept for {int(readit[curnum+1])} second(s)\n")
        except ValueError:
            print(f"\nERROR: Char {curnum}: An integer is required for sleeping")
            exit()
    
    if lookinfortxt:
        txtfound += readit[curnum]

    curnum += 1
