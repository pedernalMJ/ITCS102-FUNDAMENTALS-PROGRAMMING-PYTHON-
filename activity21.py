Dirty = True 

while Dirty == True:
    cfrm = input("Do you wish to continue washing ? (y/n): ").lower()

    if cfrm == "y":
        print("Loop Continue")
        continue 
    elif cfrm == "n":
        print("Loop Stops")
        break
    else:
        print("invalid choice")
        continue