#! python

from sys import argv, stdout
from time import sleep
from os import remove
from files.shell import shell
from shutil import rmtree

ver = "3.25" # format: major potscr release number (dot) commit number

using_py = False
script_ok = False
lookinfortxt = False
shell_ok = False
logit = False
len = 0
curnum = 0
storednum = 0
txtfound = ""
stored = ""
logpath = ""
ifcode = ""

helptxt = f"""

potatoscript parser v{ver}    

usage: potscr [-s] [-h] (input file) [-l (log file)]

arguments:

-h,--help: shows help
-l,--logpath (log file): sets a path for the log file
-s,--shell: interactive potatoscript shell

    """
noargtxt = f"""

potatoscript parser v{ver}

for help, type 'potscr --help' or 'potscr -h'
            
            """
try:
    rmtree("files\__pycache__")
except:
    pass

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
    # print(tempnum,i) -- for debugging
    if i == "--logpath" or i == "-l":
        logit = True
        try:
            logpath = argv[tempnum+1]
            logfile = open(logpath,"x")
        except FileExistsError:
            remove(logpath)
            logpath = argv[tempnum+1]
            logfile = open(logpath,"x")
        except IndexError:
            print("ERROR: no path specified for log file")

if "-s" in argv or "--shell" in argv:
    shell_ok = True
    

if using_py:
    if argv[1].endswith(".potscr") or argv[1].endswith(".potato") or argv[1].endswith(".pscr"):
        file = open(argv[1],"r")
        readit = file.read()
        if not readit.startswith("~"):
            print("ERROR: This is not a potatoscript file! Did you forget the ~ in the beginning?")
            exit()
        else:
            if not readit.endswith("~"):
                print("ERROR: This file has no ending indicator!")
                exit()
            
else:
    if argv[0].endswith(".potscr") or argv[0].endswith(".potato") or argv[0].endswith(".pscr"):
        file = open(argv[0],"r")
        readit = file.read()
        if not readit.startswith("~"):
            print("ERROR: This is not a potatoscript file! Did you forget the ~ in the beginning?")
            exit()
        else:
            if not readit.endswith("~"):
                print("ERROR: This file has no ending indicator!")
                exit()



if shell_ok:
    shell()

        

# when this is updated, copy-paste into shell.py

if not shell_ok:
    if logit:
        def log(txt):
            logfile.write(txt)
    def mathsomethin(type):
        if lookinfortxt:
            pass
        else:
            global storednum
            if readit[curnum+1] == "%":
                if readit[curnum+2].isnumeric():
                    if type == "+":
                        storednum += int(readit[curnum+2])
                    elif type == "-":
                        storednum -= int(readit[curnum+2])
                    elif type == "*":
                        storednum = storednum * int(readit[curnum+2])
                    elif type == "/":
                        storednum = storednum / int(readit[curnum+2])

                    if logit:
                        if type == "+":
                            log(f"LOG: added {int(readit[curnum+2])} to storednum (now {storednum})\n")
                        elif type == "-":
                            log(f"LOG: subtracted {int(readit[curnum+2])} from storednum (now {storednum})\n")
                        elif type == "*":
                            log(f"LOG: multiplied {int(readit[curnum+2])} by storednum (now {storednum})\n")
                        elif type == "/":
                            log(f"LOG: divided {int(readit[curnum+2])} by storednum (now {storednum})\n")
                else:
                    if type == "+":
                        storednum += 5
                    elif type == "-":
                        storednum -= 5
                    elif type == "*":
                        storednum = storednum * 5
                    elif type == "/":
                        storednum = storednum / 5

                    if logit:
                        if type == "+":
                            log(f"LOG: added 5 to storednum (now {storednum})\n")
                        elif type == "-":
                            log(f"LOG: subtracted 5 from storednum (now {storednum})\n")
                        elif type == "*":
                            log(f"LOG: multiplied 5 by storednum (now {storednum})\n")
                        elif type == "/":
                            log(f"LOG: divided 5 by storednum (now {storednum})\n")
            else:
                if type == "+":
                    storednum += 1
                elif type == "-":
                    storednum -= 1
                elif type == "*":
                    storednum = storednum * 1
                elif type == "/":
                    storednum = storednum / 1

                if logit:
                    if type == "+":
                        log(f"LOG: added 1 to storednum (now {storednum})\n")
                    elif type == "-":
                        log(f"LOG: subtracted 1 from storednum (now {storednum})\n")
                    elif type == "*":
                        log(f"LOG: multiplied 1 by storednum (now {storednum})\n")
                    elif type == "/":
                        log(f"LOG: divided 1 by storednum (now {storednum})\n")


    for i in range(0,readit.__len__()):
        char = readit[curnum]
        if char == "-": # start of print
            lookinfortxt = True
            if logit:
                log("LOG: print start\n")
        elif char == "_": # end of print
            lookinfortxt = False
            try:
                if readit[curnum+1] == "%": # percentage after means an alt version of the command, in this case no newline
                    stdout.write(txtfound[1:])
                    stdout.flush()
                    if logit:
                        log("LOG: print end (no newline)\n")
                        log(f"LOG: printed {txtfound[1:]}\n")
                    txtfound = ""
                else:
                    print(txtfound[1:])
                    if logit:
                        log("LOG: print end\n")
                        log(f"LOG: printed {txtfound[1:]}\n")
                    txtfound = ""
            except IndexError:
                print(txtfound[1:])
                if logit:
                    log("LOG: print end\n")
                    log(f"LOG: printed {txtfound[1:]}\n")
                txtfound = ""
        elif char == "#": # get input
            if lookinfortxt: # if compiling the string to be printed, don't get input
                pass
            else:
                temp = input()
                if temp.isnumeric() and readit[curnum+1] == "%":
                    storednum = int(temp)
                    if logit:
                        log("LOG: got input from user\n")
                        log(f"LOG: storednum = {storednum}\n")
                elif readit[curnum+2] == "!" and readit[curnum+1] == "%":
                    stored = stored+temp
                    if logit:
                        log(f"LOG: appended {temp} to stored, now {stored}")
                elif readit[curnum+1] == "%" and not temp.isnumeric():
                    print("ERROR: Input must be an integer!")
                    if logit:
                        log("ERROR: Input must be an integer!")
                    exit()
                else:
                    stored = temp
                    if logit:
                        log("LOG: got input from user\n")
                        log(f"LOG: stored = {stored}\n")

        elif char == "$": # print stored var
            if lookinfortxt:
                pass
            else:
                print(stored,end="")
            if logit:
                log(f"LOG: printed stored ({stored})\n")
        elif char == "/": # newline
            print("")
            if logit:
                log("LOG: printed newline\n")
        elif char == "*": # reset stored number
            if lookinfortxt:
                pass
            else:
                storednum = 0
                if logit:
                    log("LOG: storednum reset\n")
        elif char == "+": # number +
            mathsomethin("+")
        elif char == "`": # number -
            mathsomethin("-")
        elif char == ">": # number multiplied
            mathsomethin("*")
        elif char == "&": # number divided
            mathsomethin("/")
        elif char == "^": # print stored num
            if lookinfortxt:
                pass
            else:
                if readit[curnum+1] == "%":
                    print(storednum,end="")
                else:
                    print(storednum)
            
                if logit:
                    log(f"LOG: printed storednum ({storednum})\n")
        elif char == "@": # sleep
            if lookinfortxt:
                pass
            else:
                try:
                    sleep(int(readit[curnum+1]))
                    if logit:
                        log(f"LOG: slept for {int(readit[curnum+1])} second(s)\n")
                except ValueError:
                    print(f"\nERROR: Char {curnum}: An integer is required for sleeping")
                    if logit:
                        log(f"ERROR: char {curnum}: an integer is required for sleeping\n")
                    exit()
        
        # implement if statements somehow
        # elif char == "[":
        #     lookinforendif = True
        # elif char == "]":
        #     lookinforendif = False

        elif char == "!": # force stop
            if lookinfortxt:
                pass
            else:
                if readit[curnum-2] == "#" and readit[curnum-1] == "%": # checks for input. if yea, then don't force stop.
                    pass
                else:
                    if readit[curnum+1] == "%":
                        try:
                            compnum = readit[curnum+2]
                            if int(compnum) == storednum:
                                if logit:
                                    log(f"LOG: force stop at char {curnum} becuase {storednum}={readit[curnum+2]}")
                                break
                            else:
                                if logit:
                                    log(f"LOG: compared {storednum} to {readit[curnum+2]}, result false\n")
                                pass
                        except ValueError:
                            print(f"ERROR: integer expected at char {curnum}, got {readit[curnum+2]}")
                    else:
                        if logit:
                            log(f"LOG: force stop at char {curnum}\n")
                        break


        if lookinfortxt:
            txtfound += char

        curnum += 1