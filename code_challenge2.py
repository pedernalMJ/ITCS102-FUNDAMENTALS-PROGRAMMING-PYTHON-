amount = int(input("Enter amount to deposit: "))

#MAS EASY KUNG LOOP PARA DI MANUAL
count = amount // 1000
amount %= 1000
print(f"{count} × 1000")


count = amount // 500
amount %= 500
print(f"{count} × 500")


count = amount // 200
amount %= 200
print(f"{count} × 200")


count = amount // 100
amount %= 100
print(f"{count} × 100")


count = amount // 50
amount %= 50
print(f"{count} × 50")


count = amount // 20
amount %= 20
print(f"{count} × 20")


count = amount // 10
amount %= 10
print(f"{count} × 10")


count = amount // 5
amount %= 5
print(f"{count} × 5")


count = amount // 1
amount %= 1
print(f"{count} × 1")


