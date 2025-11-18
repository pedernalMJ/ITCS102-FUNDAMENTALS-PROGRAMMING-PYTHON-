import os

os.system("cls")
print("STUDENT INFORMATION SYSTEM")
print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")

student_records = {}

while True: 
    print("Select from the options: \nA - Add Information\nB - Search a Record\nC - Delete a Record\nD - Modify a Record\nE - Exit\nP - Print All ")
    
    choice = input("Your Choice ---> ").upper()

    if choice == 'A':
        print("ADDING STUDENT INFORMATION")
        print("= = = = = = = = = = = = = = =")
        
        search_code = input("Key search for this student ---> ").upper()
        first_name = input("Type the Student's First name ---> ").upper()
        last_name = input("Type the Student's Last name ---> ").upper()
        course = input("Type the Student's Course ---> ").upper()
        email = input("Type the Student's email address ---> ")
        isSingle= input("Are you Single or Married? (S / M)--->").upper()

        student_records = {search_code : [first_name, last_name, course, email, isSingle]}
        print("DATA SAVED")

        os.system('cls')
        continue

    elif choice == 'B':
        os.system('cls')
        code = input("Type the search code - - - > ")
        
        for j in student_records.keys():
            if code in student_records.keys():
                print("Record Found . . . ")
                
                for i in student_records[code]:
                    print(i)

            else: print("No Recrod . . . ")
        continue
    elif choice =='C':
        pass
        continue
    elif choice == 'D':
        print("Editing . . . ")
        continue
    elif choice == 'E':
        print("SYSTEM EXIT")
        break
    elif choice == "P":
        for i,j in student_records.items():
            print(f"Code - {i} stored information - - - > {j}")
    else:
        print("\nInvalid choice")
        continue
