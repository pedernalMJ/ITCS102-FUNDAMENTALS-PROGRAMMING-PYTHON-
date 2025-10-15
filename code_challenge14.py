name =input("Enter name -->")
print(f"Hi ! what is your name -->{name}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("ODD number compiler, type 0 to terminate the loop")
oddsum = 0
odd = ""

while True:
    num = eval(input("Enter number-->"))
    if num == 0:
        print("terminated loop")
        break
    if num % 2 == 1:
        oddsum += num
        odd += str(num) +","
        print("ODD Number detected")
        continue
    else:
        print("invalid number")
        continue
print(f"Hi {name}, The sum of all ODD number is {oddsum}")

print(f"All the ODD numbers you input is {odd}")
