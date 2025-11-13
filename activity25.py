from activity23 import *


# Creating a Menu with While Loop and Functions
name = input("Hi, what is your name --> ")
print(f"Welcome {name}, to my Compiler Program!")

isContinue = True

while isContinue:
    print("Select a program")
    print("A - Activity1\nB - Activity2\nC - Activity3\nD - Activigty 4\nE - Exit")

    choose = input("What program/code would you like to run --> ").lower()

    if choose == 'a':
        activity1()
        continue

    elif choose == 'b':
        activity2()
        continue

    elif choose == 'c':
        activity3()
        continue

    elif choose == 'd':
        activity4()
     
        continue

    elif choose == 'e':
        print("Thank you for using the Compiler Program!")
        break
    else:
        print("Invalid option! Please try again.")
