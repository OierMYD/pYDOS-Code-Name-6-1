#INCLUDES
from random import*
from time import*
from os import*
#STRINGDATAS
logo = """
|-----------------------------------------------|
|  |-----|                uY Soft               |
|  |   u |               Pythonix               |
|  |-----|-----|        pY-DOS(R)               |
|        |  Y  |             Beta               |
|        |-----|-----   CodeName   6 + 1        |
|              |            Built on            |
|    pY-DOS    |    New Technology  1.2.3768    |
|-----------------------------------------------|
"""
logoData = """
|  -|
|   |    
|   |
|------|
|      |  
|      |
|------|
"""
#DEFS
def c():
    sleep(0.5)
    system("cls")
def vtdos():
    print("Virtual-DOS Free Edition 1.01")
    print("------------------------------------------------")
    v = input("VTDOS:>")
    if v == "exit":
        c()
        pass
        
def whatnew():
    print("What is new in pY-DOS Code 6+1?")
    print("------------------------------------------------")
    print("1.Updated Core(1.1 to 1.2)")
    print("2.Add Virtual-DOS Free Edition")
    print("3.Updated UI")
    print("------------------------------------------------")
    what = input("Local:>")
    c()
def helloscr():
    print("pYDOS Hello Screen:>")
    print("------------------------------------------------")
    print("Hello!")
    print("Hi!")
    print("Hola!")
    print("Bonjour!")
    print("------------------------------------------------")
    print("(Press <Enter> key to log in.)")
    log = input("Log:>")
    c()
def dos():
    print(logo)
    sleep(2)
    c()
    whatnew()
    helloscr()
    while True:
        print("------------------------------------------------")
        print("Pythonix pY-DOS (6+1) Options Menu:>")
        space1 = "------------------------------------------------"
        print(space1)
        print("Settings:>")
        space2 = "                                                "
        print(space2)
        print("1.About pY-DOS")
        print(space1)
        print("Apps & Docs:>")
        print(space2)
        print("2.Calculator.py")
        print("3.GuessingNumbers.py")
        print("4.Virtual-DOS Free")
        print("5.Exit")
        print(space1)
        print("6.PyShell 1.2(For pY-DOS)")
        print(space1)
        op = int(input("Local:>"))
        c()
        if op == 4:
            vtdos()
        elif op == 6:
            print("PyShell 1.2:>")
            print(space1)
            print("1.PowerShell")
            print("2.CMD")
            print("3.EXPLORER")
            print("4.MSconfig")
            print("5.Calc")
            print(space1)
            i = int(input("C:\Windows\System32\\"))
            if i == 1:
                system("start powershell")
            elif i == 2:
                system('start cmd')
            elif i == 3:
                system("start explorer")
            elif i == 4:
                system("start msconfig")
            elif i ==5:
                system("start calc")
            elif i == 6:
                print(space1)
                print("PyShell")
                print("Version 1.2.1")
                print("For pY-DOS API")
                print(space2)
                print("Standard Edition")
                print(space1)
                print("Unknown Y Software Studio")
                print("Copyright(c)All rights reserved.")
                sleep(2.5)
            else:
                print("  ")
                pass
            c()    
        elif op == 5:
            break
        elif op == 1:
            print(logoData)
            print("Pythonix pY-DOS Beta Logic")
            print("Standard Edition(Free)")
            print("Pythonix Core:")
            print("Pythonix Version 1.2.3768")
            print(space1)
            print("Quit(exit)")
            choice2 = input("Local:>About>")
            if choice2 =="exit":
                c()
            pass
        elif op == 2:
            print("----------Calculator.py----------")
            print("Choose a way:")
            print("1=+ 2=- 3=* 4=/")
            ways = int(input("Way:"))
            num1 = int(input("The first number is:"))
            num2 = int(input("The second number is:"))
            if ways == 1:
                print(num1 + num2)
            elif ways == 2:
                print(num1 - num2)
            elif ways == 3:
                print(num1 * num2)
            else:
                print(num1 / num2)
            c()    
        elif op == 3:
            print("-----GuessingNumbers.py-----")
            print("The number is from 1 to 100.")
            answer = randint(1,100)
            while 1:
                i = int(input("Guess:"))
                if i > answer:
                    print("It is big.")
                elif i < answer:
                    print("It is small.")
                else:
                    print("Great!")
                    sleep(0.5)
                    break
            c()    
        else:
            print("Wrong letters.Type again.")
dos()    
