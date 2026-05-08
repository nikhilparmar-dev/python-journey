# Class And Object :
from mimetypes import init
from unicodedata import name


class Student :
    pass # empty for now


# init - Constructor : Runs when Object is Created
class Student :
    def __init__(self, name, age, city) :
        self.name = name
        self.age =  age
        self.city = city

s1 = Student("Nikhil", 17, "Kadi")
s2 = Student("Prem", 18, "Ahmedabad")

print(s1.name)
print(s2.city)



# Methods - Function inside class :
class Person :
    def __init__(self, name, age):
         self.name = name
         self.age = age

    def introduce(self) :
        print(f"Hii, i'm {self.name}, and i'm {self.age} years old")

    def is_Adult(self) :
        if self.age >= 18 :
            return True
        else :
            return False

p = Person("Nikhil", 17)
p.introduce()
print(p.is_Adult())




# Four Pillers of OOP's :

# 1. Encapsulation : Hindes Private Details
class Bank : 
    def __init__(self, balance) :
        self.__balance = balance    # __ means private variable

    def deposit(self, amount) :
        self.__balance += amount

    def getbalance(self) :
        return self.__balance   # Controlled Here

b = Bank(5000)
b.deposit(3000)
# print(b.__balance)  # Gives Error
print(b.getbalance())



# Inheritance : 
class Person :  # Parent class
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def introduce(self) : 
        print("I'm ", self.name)

class Developer(Person) :
    def __init__(self, name, age, language) :
        super().__init__(name, age) # Calls Parent class

        self.language = language
        
    def show_skills(self) :
        print(f"{self.name} codes in {self.language}")

p = Developer("Nikhil", 17, "Java")
p.introduce()
p.show_skills()


# 3. Polymorphism - Same names, different behaviour

class Dog :
    def speak(self) :
        return "Bhow Bhow"

class Cat :
    def speak(self) :
        return "Meaw Meaw..."

class Duck :
    def speak(self) :
        return "Quack"

animals = [Dog(), Cat(), Duck()]

for animal in animals :
    print(animal.speak())


# 4. abtraction - show's only needed details

class Bank :
    def __validatePin(self) :
        print("Validating Pin...")

    def __connectbank(self) :
        print("Connecting to bank...")

    def withdraw(self, amount) :
        self.__validatePin()
        self.__connectbank()

        print("Done")

B = Bank()
B.withdraw(5000)



# 5. __str function :
class Person :
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def __str__(self) :
        return f"Name = {self.name}, Age= {self.age}"

p = Person("Nikhil", 17)
print(p)
