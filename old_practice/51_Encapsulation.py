# WAP to show the use of Encapsulation in python.
# Date: 09/03/2026
# Author: Nikhil    


# Restrict access to certain attributes or methods to protect data and enforce controlled access

# Example 1 :
class Student :
    def __init__(self, name, grade, percentage):
        self.name = name
        self.grade = grade
        self.__percentage = percentage     # limited access

    def get_percentage (self) :
        return self.__percentage
    
    def student_details (self) :
        print(f"{self.name} is in class {self.grade}, with {self.__percentage}%")

s1 = Student("Nikhil", 12, 91.00)
s2 = Student("Prem", 11, 81.20)

# print(s1.percentage)    # shows error
print(s2.get_percentage())
s1.student_details()




# Example 2 :
class Student :
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks


    # getter
    def getMarks (self) :
        return self.__marks
    
    # setter
    def setter (self, marks) :
        if marks >= 0 <= 100 :
            self.__marks = marks

        else :
            print("Invalid Marks")


s1 = Student("Zeeshan", 87)

print("Name: ", s1.name)
print("Marks: ", s1.getMarks())

s1.setter(90)
print("Updated marks: ", s1.getMarks())





# Example 3 :
class Employee :

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def getSalary (self) :
        return self.__salary
    
    def setSallary (self, salary) :
        if salary > 0 :
            self.__salary = salary

    def show (self) :
        print("Name: ", self.name)
        print("Salary: ", self.__salary)


e = Employee("Nirmesh", 69000)

e.show()