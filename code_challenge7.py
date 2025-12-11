#Sir check MONA LANG HISTORY DIPO AKO NANG GAYA 5 HOURS AGO KO PAPO TO GINAWA 
print("ODD NUMBER SUMMATION")
num = eval(input("Enter a number: "))

oddsum = 0

for i in range(10):
    if num % 2 == 1:
        oddsum += num  

print("The sum of all the ODD numbers is", oddsum)
