months = ["jan", "feb", "mar", "apr", "may", "jun", "jul"]

# add item to the end
months.append("aug")
print(months)

# remove last item
months.pop(1)
print(months)

# remove a specific item
months.remove("mar")
print(months)

# insert a new item at index 4
months.insert(4, "new")
print(months)

# show the length of the list
lenlist = len(months)
print("Length of list:", lenlist)

# sort the list alphabetically
months.sort()
print("Sorted list:", months)

# iteration
for m in months:
    print(f"{m},2025")


fullname = 'mark juben pedernal'

# #list slicing / reverse name
print(fullname[::-1])