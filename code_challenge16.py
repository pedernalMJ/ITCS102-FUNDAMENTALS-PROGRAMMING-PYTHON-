import os

os.system("cls")
print("STUDENT INFORMATION SYSTEM")
print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")

student_records = {}

while True: 
    print("Select from the options: \nA - add student reocerd\nB - print all records\nC - search records\nD - delete record\nE - Edit student record\nF - exprot data\nG - exit ")
    
    choice = input("Your Choice ---> ").upper()

    if choice == 'A':
        print("ADDING STUDENT INFORMATION")
        print("= = = = = = = = = = = = = = =")
        
        studentid = input("Key search for this student ---> ").upper()
        first_name = input("Type the Student's First name ---> ").upper()
        last_name = input("Type the Student's Last name ---> ").upper()
        course = input("Type the Student's Course ---> ").upper()
        email = input("Type the Student's email address ---> ")
        isSingle= input("Are you Single or Married? (S / M)--->").upper()

        student_records = {studentid : [first_name, last_name, course, email, isSingle]}
        print("DATA SAVED")

        os.system('cls')
        continue

    elif choice == 'B':
        print("Printing Student Records")
        for id,record in student_records.items():
            print(f"Student id {id} in Student record {record}")
        continue
    elif choice =='C':
        os.system("cls")
        print("SEARCH STUDENT RECORD")

        search_id= input("input id to search-->").upper()

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("=====================")
                print("\n\nRecord found")
                print("=====================")
                for i in student_records[search_id]:
                    print(f"-- {i}")
        else:
            print("no record found")
        pass
        continue
    elif choice == 'D':
        os.system("cls")
        print("Delete existing record")

        search_id = input("INPUT ID TO SEARCH-->").upper()
        if search_id in student_records.keys():
            print("=====================")
            print("\n\nRecord found")
            print("=====================")
            for i in student_records[search_id]:
                print(f"-- {i}")
            student_records.pop(search_id)
            print("delete . . . ")
        else:
            print("=====================")
            print("\nNo Record found")
            print("=====================")

        continue
    elif choice == 'F':
        print("export")  
    elif choice == "G":
        print("exiting")
        break
        
    else:
        print("\nInvalid choice")
        continue
