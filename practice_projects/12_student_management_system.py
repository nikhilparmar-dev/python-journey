# Mini Project #12 -  Student Management System (Dictionary)
# Date: 05/03/2026
# Author: Nikhil


students = {}

while True : 

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Fees Collected")
    print("7. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1 :

        id = int(input("Enter Student Id: "))
        name = input("Enter Student Name: ")
        course = input("Enter Student Course: ")
        fees = int(input("Enter Student Fees: "))

        students[id] = {
            "Name" : name,
            "Course" : course,
            "Fees" : fees
        }

        print("Student Added Successfully!")



    elif choice == 2 :

        print("\n--- Students List ---")

        for id, info in students.items() :
            print(f"Id: {id} | Name: {info["Name"]} | Course: {info["Course"]} | Fees: {info["Fees"]}")



    elif choice == 3 : 

        id = int(input("Enter Student Id To search: "))

        if id in students :
            info = students[id]
            print("Found : ", info)

        else :
            print("Student Not Found!")



    elif choice == 4 : 

        id = int(input("Enter Student Id To search: "))

        if id in students :
            students[id]["Name"] = input("Enter New Name: ")
            students[id]["Course"] = input("Enter New Course: ")
            students[id]["Fees"] = int(input("Enter New Fees: "))

            print("Student Updated Successfully!")

        else :
            print("Student Not Found!")



    elif choice == 5 : 
        
        id = int(input("Enter Student Id To delete: "))

        if id in students :
            students.pop(id)
            print("Student Deleted Successfully")

        else :
            print("Student Not Found!")



    elif choice == 6 : 

        total = sum(student["Fees"] for student in students.values())

        print("Total Fees Collected: ", total)



    elif choice == 7 : 

        print("Thank You")
        break


    else :

        print("Invalid Choice! ")