# Mini Project #14 - Vehicle Management System (Abtraction)
# Date: 09/03/2026
# Author: Nikhil



from abc import ABC, abstractmethod

class Vehicle (ABC) :

    def __init__(self, name, price) :
        self.name = name
        self.price = price

    @abstractmethod
    def show_details (self) :
        pass


class Car (Vehicle) :

    def show_details(self):
        print("Vehicle Type: Car")
        print("Car name: ", self.name)
        print("Car Price: ", self.price)


class Bike (Vehicle) :

    def show_details(self):
        print("Vehicle Type : Bike")
        print("Bike name: ", self.name)
        print("Bike Price: ", self.price)


class Truck (Vehicle) :

    def show_details(self):
        print("Vehicle Type: Truck")
        print("Truck name: ", self.name)
        print("Truck Price: ", self.price)


# Creating object
c = Car("Bugati", 2700000)
b = Bike("HayaBhusa", 2100000)
t = Truck("Tata Truck", 12000000)

print("--- Vehicle Details ---")

c.show_details()
print()

b.show_details()
print()

t.show_details()
print()