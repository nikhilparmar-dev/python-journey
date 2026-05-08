# WAP to show the use of Strings in python.
# Date: 04/02/2026
# Author: Nikhil

name = "Nikhil"
print(name)
print(type(name))

print("Hello'Nik")
print('''it's Me "Nikhil"''')
print("my name is \"Nikhil\"")

# Formatted Strings - insert variables or experssions
#1. Old style formatting - % operator 
age = 17
print("My name is %s & i'm %d years old." % (name, age))


#2. str.format() method
print("My name is {} and i'm {} years old.".format(name, age))
print("My name is {1} and i'm {0} years old.".format(name, age))
print("My name is {name} and i'm {age} years old.".format(name = "Prem", age = 18))


#3. f-strings

print(f"My name is {name} & i'm {age} years old.")
print(f"My age after 5 years will be {age + 5}")


# 4. Escape Characters - backslash with chars 
print("Hello\nWorld")
print("Hello\tWorld")


# 5. String Operators in Python 
a = "Hello"
b = "Python"

print(a+b)
print(a*3)

if "h" in a :
    print("Yessss")
else :
    print("No")

if "h" not in a :
    print("Yessss")
else :
    print("Nooo")

print(r"hello \n\t world")