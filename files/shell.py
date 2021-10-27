from sys import stdout
from time import sleep
from os import system

storednum = 0

def shell():
    global storednum
    txtfound = ""
    curnum = 0
    lookinfortxt = ""
    firstTime = True
    stored = ""
    shellver = 1.4

    try:
        system("cls")
    except:
        print("\n\n")

    while True:
        curnum = 0
        shellIn = ""
        if firstTime:
            print(f"potscr shell v{shellver}\n")
            print("type 'quit' to exit.")
            firstTime = False

        shellIn = input("> ")
        if shellIn == "quit" or shellIn == "q" or shellIn == "bye" or shellIn == "exit":
            exit()

        # code in potscr.py starts here

        def mathsomethin(type):
            global storednum
            if lookinfortxt:
                pass
            else:
                try:
                    if shellIn[curnum+1] == "%":
                        if shellIn[curnum+2].isnumeric():
                            if type == "+":
                                storednum += int(shellIn[curnum+2])
                            elif type == "-":
                                storednum -= int(shellIn[curnum+2])
                            elif type == "*":
                                storednum = storednum * int(shellIn[curnum+2])
                            elif type == "/":
                                storednum = storednum / int(shellIn[curnum+2])
                        else:
                            if type == "+":
                                storednum += 5
                            elif type == "-":
                                storednum -= 5
                            elif type == "*":
                                storednum = storednum * 5
                            elif type == "/":
                                storednum = storednum / 5                
                except IndexError:
                    if type == "+":
                        storednum += 1
                    elif type == "-":
                        storednum -= 1
                    elif type == "*":
                        storednum = storednum * 1
                    elif type == "/":
                        storednum = storednum / 1



        for i in range(0,shellIn.__len__()):
            char = shellIn[curnum]
            if char == "-": # start of print
                lookinfortxt = True
            elif char == "_": # end of print
                lookinfortxt = False
                try:
                    if shellIn[curnum+1] == "%": # percentage after means an alt version of the command, in this case no newline
                        stdout.write(txtfound[1:])
                        stdout.flush()
                        txtfound = ""
                    else:
                        print(txtfound[1:])
                        txtfound = ""
                except IndexError:
                    print(txtfound[1:])
                    txtfound = ""
            elif char == "#": # get input
                if lookinfortxt:
                    pass
                else:
                    temp = input()
                    try:
                        if temp.isnumeric() and shellIn[curnum+1] == "%":
                            storednum = int(temp)
                        elif shellIn[curnum+2] == "!" and shellIn[curnum+1] == "%":
                            stored = stored+temp
                        elif shellIn[curnum+1] == "%" and not temp.isnumeric():
                            print("ERROR: Input must be an integer!")
                            exit()
                        else:
                            stored = temp
                    except:
                        stored = temp

            elif char == "$": # print stored var
                print(stored,end="")
            elif char == "/": # newline
                print("")
            elif char == "*": # reset stored number
                storednum = 0
            elif char == "+": # number +
                mathsomethin("+")
            elif char == "`": # number -
                mathsomethin("-")
            elif char == ">": # number multiplied
                mathsomethin("*")
            elif char == "&": # number divided
                mathsomethin("/")
            elif char == "^": # print stored num
                try:
                    if shellIn[curnum+1] == "%":
                        print(storednum,end="")
                    else:
                        print(storednum)
                except IndexError:
                    print(storednum)
               
            elif char == "@": # sleep
                if lookinfortxt:
                    pass
                else:
                    try:
                        sleep(int(shellIn[curnum+1]))
                    except ValueError:
                        print(f"\nERROR: Char {curnum}: An integer is required for sleeping")
                        exit()
            elif char == "!":
                if lookinfortxt:
                    pass
                else:
                    try:
                        if shellIn[curnum+1] == "%":
                            try:
                                compnum = shellIn[curnum+2]
                                if int(compnum) == storednum:
                                    break
                                else:
                                    pass
                            except ValueError:
                                print(f"ERROR: integer expected at char {curnum}, got {shellIn[curnum+2]}")
                            except IndexError:
                                print(f"ERROR: % found, but no char found afterwards.")
                        else:
                            break
                    except IndexError:
                        break
            
            if lookinfortxt:
                txtfound += char

            curnum += 1