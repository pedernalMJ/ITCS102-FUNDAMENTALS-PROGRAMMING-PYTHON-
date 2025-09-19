#ign1 = 'mark'
#ign2 = 'juben'
#ign3 = 'pedernal'

#print("my name is", ign1," ", ign2," ", ign3)
#print(f"my name is {name1} {name2} {name3}")

odd_sum = 0
for i in range(1, 11, 1):
    num = eval(input(f"{i} - Enter a number - - > "))
    if num % 2 == 1:
        odd_sum += num
print(f"The sum of all the ODD numbers given is:", {odd_sum})
