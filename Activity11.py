temp = eval(input("Enter temperature --> "))

if temp < 1: 
    print("Temperature freezing cold")
elif temp >= 1 and temp <= 20:
    print("Temperature cold")
elif temp >= 21 and temp <= 30:
    print("Temperature lukewarm")
elif temp >= 31 and temp <= 40:
    print("Temperature warm")
elif temp >= 41 and temp <= 50:
    print("Temperature hot")
elif temp >= 51:
    print("Temperature above boiling hot")
else:
    print("Invalid temperature")
  
