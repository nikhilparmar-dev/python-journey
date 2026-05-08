# Define a class Person and its two child classes: Male and Female. All classes have a
# method "getGender" which can print "Male" for Male class and "Female" for Female class.
# Date : 09/03/2026
# Author : Nikhil


class Person:

    def getGender(self):
        return "Unknown"


class Male(Person):

    def getGender(self):
        return "Male"


class Female(Person):
    
    def getGender(self):
        return "Female"


person = Person()
male = Male()
female = Female()

print(person.getGender())  
print(male.getGender())    
print(female.getGender()) 