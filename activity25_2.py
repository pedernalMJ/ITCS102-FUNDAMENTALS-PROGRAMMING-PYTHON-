def activity4():
    num = eval(input("enter a number"))
    factorial_value = 1
    for i in range(num, 0, -1):
        factorial_value *= i
    print(f"the factorial of{num}is{factorial_value}")
