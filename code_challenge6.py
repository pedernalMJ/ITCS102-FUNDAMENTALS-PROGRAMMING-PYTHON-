nim = int(input("Enter a number: "))
fact = 1

for i in range(1, nim + 1):
    fact = fact * i

print("The factorial of", nim, "is", fact)
