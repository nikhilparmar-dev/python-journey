# WAP to show the use of Polymorphism in python.
# Date: 10/03/2026
# Author: Nikhil    


# allows methods in difft classes to have same name but difft behaviour depending on objects 


# Example 1 :
class Dog :
    def sound(self) :
        print("Bhau Bhau...")

class Cat :
    def sound(self) :
        print("Meow Meow...")

d = Dog()
c = Cat()

d.sound()
c.sound()




# Example 2 :
class Car :
    def move(self) :
        print("Car runs on road..")

class Plane :
    def move(self) :
        print("plane flies in the sky..")

class Boat :
    def move(self) :
        print("Boat sails in water..")

c = Car()
p = Plane()
b = Boat()

c.move()
p.move()
b.move()




# Example 3 (Loop Polymorphism) :
class India :
    def capital(self) :
        print("Delhi")

class USA :
    def capital(self) :
        print("Washington DC")

obj1 = India()
obj2 = USA()

for country in (obj1, obj2) :
    country.capital()