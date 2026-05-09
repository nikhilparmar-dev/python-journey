# Mini Project #7 -  Computer Institute Management (Lists)
# Date: 23/02/2026
# Author: Nikhil


Students = []

while True :

    print("\n --- Computer Institute Management ---")
    print("1. Add Students")
    print("2. View All Students")
    print("3. Search Students")
    print("4. Total Fees Collected")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1 :
        name = input("Enter Student Name: ")
        course = input("Enter Student Course: ")
        fees = int(input("Enter Fees: "))

        student = [name, course, fees]
        Students.append(student)

        print("Student Added Successfully !")


    elif choice == 2 :
        print("\nStudent Records: ")

        for s in Students :
            print(f"Name: {s[0]} | Course: {s[1]} | Fees: {s[2]}")


    elif choice == 3 :
        search_name = input("Enter Name to search: ")
        found = False

        for s in Students :
            if s[0] == search_name : 
                print("Found in Record: ")
                print(f"Name: {s[0]} | Course: {s[1]} | Fees: {s[2]}")
                found = True

        if not found :
            print("Student not Found !")


    elif choice == 4 :
        total = 0

        for s in Students :
            total += s[2]

        print("Total Fees Collected: ", total)


    elif choice == 5 :
        print("Exiting program...")
        break


    else :
        print("Invalid Choice!")