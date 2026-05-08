# WAP to show the use of Strings in python -2 .
# Date: 05/02/2026
# Author: Nikhil

# 1. String Indexing

myName= "Nikhil Parmar" #Index: 0,1,2,3,4,5

print(myName[0])
print(myName[1])
print(myName[2])
print(myName[3])
print(myName[4])
print(myName[5])

print(myName[-1]) # last character from string
print(myName[-3]) # third last character from string

# 2. String Slicing 

print(myName[0:3])
print(myName[0:3:2])
print(myName[0:5:3])
print(myName[2:4])
print(myName[-1:])
print(myName[5:])
print(myName[-3:])
print(myName[0::2])
print(myName[:])
print(myName[::])
print(myName[::-1])


# 3. String Methods

print(len(myName))
print(myName.upper())
print(myName.lower())
print(myName.count('i'))
print(myName.find('k'))
print(myName.capitalize())
print(myName.split(','))
print(myName.split())
print(myName.replace("Nikhil", "Prem"))
print(myName.title())
print(myName.strip())
words = ("Python", "is", "best")
print(" ".join(words))
print("_".join(words))
surName = "My name is"
print(surName + " " + myName) # Concatenation

# String with loop 

for n in myName :
    print(n)
    