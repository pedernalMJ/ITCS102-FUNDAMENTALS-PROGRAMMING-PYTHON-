print("MULTIPLICATION TABLE MAKER")
nim = eval(input("Enter a number: "))

print("\nMultiplication table for", nim, ":")
for i in range(1,11):
  print(nim,"x",i,"=",nim * i)