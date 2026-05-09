# Mini Project #11 - Smart Course Enrollment System (List & Tuple)
# Date: 02/03/2026
# Author: Nikhil


# Fixed course data (unchangable)
courses = (
    ("CCC", 3900),
    ("Tally", 4500),
    ("Python", 6000)
)


# Dynamic students list (Changable)
students = []


while True :

    print("\n===== SMART COURSE ENROLLMENT SYSTEM =====")
    print("1. Show Courses")
    print("2. Enroll Student")
    print("3. View Enrolled Students")
    print("4. Total Fees Collected")
    print("5. Exit")

    choice = int(input("Enter your choice(1-5): "))

    if choice == 1 :

        print("\nAvailable Courses: ")

        for i in range(len(courses)) :
            print(f"{i+1}. {courses[i][0]} - ₹{courses[i][1]}")


    elif choice == 2 :

        name = input("Enter Student Name: ")

        print("\nSelect Course: ")
        for i in range(len(courses)) :
            print(f"{i+1}. {courses[i][0]} - ₹{courses[i][1]}")

        courseChoice = int(input("Enter Course number: "))

        if 1 <= courseChoice <= len(courses) :
            selectedCourse = courses[courseChoice - 1]
            students.append((name, selectedCourse[0], selectedCourse[1]))
            print("Student Enrolled Successfully!")

        else :
            print("Invalid course selection")


    elif choice == 3 :

        if len(students) == 0 :
            print("No students enrolled yet!")

        else :
            print("\nEnrolled Students: ")
            for s in students :
                print(f"Name: {s[0]}, Course: {s[1]}, Fees: ₹{s[2]}")

    
    elif choice == 4 :

        total = 0 
        for s in students :
            total += s[2]

        print(f"Total Fees Collected ₹{total}")


    elif choice == 5 :

        print("Thank You")
        break

    
    else :

        print("Invalid choice! please try again")