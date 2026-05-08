# WAP to show the use of Abtraction in python.
# Date: 07/03/2026
# Author: Nikhil



# Hiding unneccesary details from the users using class methods.

# Example 1 :

class Student :
    def __init__(self, name, grade, percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage

    def student_details(self) :
        print(f"Name: {self.name} | Grade: {self.grade} | Percentage: {self.percentage}%")      # hidden from users

student1 = Student("Nikhil", 'O', 91)
student2 = Student("Prem", 'A', 84)

student1.student_details()
student2.student_details()




# Example 2 :
from abc import ABC, abstractmethod

class Shape(ABC) :      # Parant class
    @abstractmethod
    def area(self) :
        pass

class Rectangle :       # Child class
    def __init__(self, length, width) :
        self.length = length
        self.width = width

    def area(self) :
        return self.length * self.width
    
class Circle :
    def __init__(self, radius):
        self.radius = radius

    def area(self) :
        return 3.14 * self.radius * self.radius
    
r = Rectangle(5, 10)
c = Circle(7)

print("Area of Rectangle: ", r.area())
print("Area of Circle: ", c.area())




# Example 3 :
from abc import ABC, abstractmethod

class Vehicle :
    @abstractmethod
    def start(self) :
        pass

class Car(Vehicle) :
    def start(self) :
        print("car starts with key and buttton")

class bike(Vehicle) :
    def start(self):
        print("Bike starts with cick and self start")

class Truck(Vehicle) :
    def start(self):
        print("Truck starts with heavy engin ignition")

c = Car()
b = bike()
t = Truck()

c.start()
b.start()
t.start()