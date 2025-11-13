from  import *

# Creating a Menu with While Loop and Functions
name = input("Hi, what is your name --> ")
print(f"Welcome {name}, to my Compiler Program!")

isContinue = True

while isContinue:
    print("\nSelect a Program")
    print("a - Activity1")
    print("b - Activity2")
    print("c - Add Odd Numbers")
    print("d - Factorial Program")
    print("e - Exit")

    choose = input("What program/code would you like to run --> ").lower()

    if choose == 'a':
        activity1()
        continue

    elif choose == 'b':
        activity2()
        continue

    elif choose == 'c':
        add_odd()
        continue

    elif choose == 'd':
        print("Factorial Program")
        num = int(input("Input a number for factorial computation: "))

        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n - 1)

        print(f"The factorial of {num} is {factorial(num)}")
        continue

    elif choose == 'e':
        print("Thank you for using the Compiler Program!")
        isContinue = False

    else:
        print("Invalid option! Please try again.")
