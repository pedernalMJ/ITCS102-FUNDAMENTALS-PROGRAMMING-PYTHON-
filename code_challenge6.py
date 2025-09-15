
nim = int(input("Enter a number: "))
fact = 1

for i in range(nim, 0, -1):
    fact = fact * i

print("The factorial of", nim, "is", fact)
