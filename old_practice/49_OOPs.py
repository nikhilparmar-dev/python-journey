# WAP to show the use of OOP (Object Oriented Programming) in python.
# Date: 06/03/2026
# Author: Nikhil


# Creating student records using OOPs :
class Student :     # Class

    def __init__(self, name, grade, percentage):    # Method (Constructor)
        self.name = name
        self.grade = grade
        self.percentage = percentage

student1 = Student("Nikhil", 'A', 91.00)    # Creating Objects
student2 = Student("Prem", 'B', 82.91)

print(student1.name, " | ", student1.grade, " | ", student1.percentage, "%")
print(student2.name, " | ", student2.grade, " | ", student2.percentage, "%")




# Two methods in a class 
class Student : 
    def __init__(self, name, age, city) :
        self.name = name
        self.age = age
        self.city = city

    def studentDetails(self) :
        print(f"{self.name} | {self.age} | {self.city}")

student3 = Student("Zeeshan", 19, "Kadi")   # Creating an Object

student3.studentDetails()   # Calling the function

print(student3.__dict__)    # Data print in dictionary type


# Modifying Object Property
print(student3.age)
student3.age = 20
print(student3.age)

# Deleting Object Property
print(student3.__dict__)
del student3.city
print(student3.__dict__)

# Deleting Object
del student3
# print(student3) # Gives error




# Basic Real Life Examples :

# 1 :-
class Student :
    def __init__(self, name, course, fees) :
        self.name = name
        self.course = course
        self.fees = fees

    def display(self) :
        print("Name: ", self.name)
        print("Course: ", self.course)
        print("Fees: ", self.fees)

s1 = Student("Khushi", "CA", 100000)
s2 = Student("Angel", "IDK", 99999)

s1.display()
print("-----------")
s2.display()



# 2 :-
class bankAccount :
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount) :
        self.balance += amount
        print("Deposited Successfully")

    def withdraw(self, amount) :
        if amount <= self.balance :
            self.balance -= amount
            print("Withdrawal Success")
        
        else :
            print("Insufficient Balance!")

    def CheckBalance(self) :
        print("Current Balance: ", self.balance)

acc1 = bankAccount("Amit", 1000)

acc1.deposit(2000)
acc1.withdraw(1200)
acc1.CheckBalance()