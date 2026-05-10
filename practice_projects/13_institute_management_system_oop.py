# Mini Project #13 - Institute Management System (OOP's)
# Date: 06/03/2026
# Author: Nikhil


class Student :
    def __init__(self, name, course, fees) :
        self.name = name
        self.course = course
        self.fees = fees

    def display(self) :
            print(f"Name: {self.name}")
            print(f"Course: {self.course}")
            print(f"Fees: {self.fees}")
            print("---------------------")



class Institute : 
    def __init__(self):
          self.students = []

    def add_student(self) :
         name = input("Enter Student Name: ")
         course = input("Enter Course Name: ")
         fees = int(input("Enter Fees: "))

         student = Student(name, course, fees)
         self.students.append(student)
         print("Student Added Successfully")

    def View_Students(self) :
        if not self.students :
              print("No Students Found!\n")

        else : 
             print("\n--- Students List ---")
             for student in self.students :
                  student.display()

    def Search_Student(self) :
         search_name = input("Enter Student name to search: ")
         found = False

         for student in self.students :
              if student.name.lower() == search_name.lower() :
                   student.display()
                   found = True
                   break
              
              if not found :
                   print("Student not found!")

    def totalFees(self) :
         total = sum(student.fees for student in self.students)
         print("Total Fees: ", total, "\n")


institute = Institute()

while True :
     print("------ Computer Institute Management ------")
     print("1. Add Student")
     print("2. View Students")
     print("3. Search Student")
     print("4. Total Fees Collected")
     print("5. Exit")

     choice = int(input("Enter Your Choice: "))

     if choice == 1 :
          institute.add_student()

     elif choice == 2 :
          institute.View_Students()

     elif choice == 3 :
          institute.Search_Student()

     elif choice == 4 :
          institute.totalFees()

     elif choice == 5 :
          print("Thank You")
          break

     else :
          print("Invalid choice")