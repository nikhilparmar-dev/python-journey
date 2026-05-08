# WAP to show the use of Inheritance in python.
# Date: 10/03/2026
# Author: Nikhil    



# allows one class (child) to reuse the prop and methods of another class (parent). 

class Student :     # Parent class
    def __init__(self, name, grade, percentage) :
        self.name = name
        self.grade = grade
        self.percentage = percentage

    def student_details(self) :
        print(f"{self.name} is in class {self.grade} with {self.percentage}%")

student1 = Student("Nikhil", "FY-BCA", 9.00)



class GraduateStudent (Student) :
    def __init__(self, name, grade, percentage, stream) :
        super().__init__(name, grade, percentage)
        self.stream = stream

    def student_details(self) :
        super().student_details()
        print(f"Stream is {self.stream}")


GradStudent = GraduateStudent("Prem", 'A', 98, "PCM")

GradStudent.student_details()





# Example 1 : 
class Animal :
    def eat(self) :
        print("Animal can eat")

class Dog (Animal) :
    def bark (self) :
        print("Dog can bark")

d = Dog()

d.eat()
d.bark()




# Example 2 :
class Vehicle :
    def start (self) :
        print("Vehicle is starting...")

class Car (Vehicle) :
    def speed (self) :
        print("Car speed is 120 kmph")

c = Car()

c.start()
c.speed()



# (Multilevel Inheritance)
# Example 3 :
class GrandFather :
    def house(self) :
        print("Grandfather House")

class Father (GrandFather) :
    def Car(self) :
        print("Father Bike")

class Son (Father) :
    def Bike(self) :
        print("Son Bike")

s = Son()

s.house()
s.Car()
s.Bike()




# (Hierarchical Inheritance)
# Example 4 :
class Animal :
    def eat(self) :
        print("Animal can eat")

class Dog (Animal) :
    def bark(self) :
        print("dog can bark")

class Cat (Animal) :
    def meow (self) :
        print("Cat can meow")

d = Dog()
c = Cat()

d.eat()
d.bark()

c.eat()
c.meow()