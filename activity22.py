import random

print("Let's guess the number")

random_number = random.randint(1, 3)
tries = 0
tuloy = True

while tuloy == True:
    num = int(eval(input("Input an integer number --> ")))

    tries += 1 

    if num == random_number: 
        print("CORRECT")
        print(f"Only took {tries} tries")
        break
    else:
        print("WRONG")
        print("Continue")
        continue
