print("ODD NUMBER SUMMATION")
num = int(input("Enter a number: "))

oddsum = 0

for i in range(10):
    if num % 2 == 1:
        oddsum += num  

print("The sum of all the ODD numbers is", oddsum)
