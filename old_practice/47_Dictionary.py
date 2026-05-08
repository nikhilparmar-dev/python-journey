# WAP to show the use of Dictionary in python.
# Date: 02/03/2026
# Author: Nikhil


# A. dictionary create methods :

# Method 1 : Using curly Bras
intro = {"Name" : "Nikhil",
         "Age" : 17,
         "Course" : "Python",
         "Level" : "Expert"
         }

print(intro)
print(type(intro))


# Method 2 : Using dict() constructor
person = dict(Name = "Nikhil", Age = 17, Grade = "O")


print(person)
print(type(person))


# Method 3 : using list of tuples 
person2 = dict([("Name", "Nikhil"), ("Age", 17), ("Grade", "O")])

print(person2)
print(type(person2))



# B. Accessing dictonary values
student = {
    1 : "Class - X",
    "Name" : "Nikhil",
    "Age" : 17,
    "City" : "Kadi"
}

print(student)
print(type[student])

print(student["Name"])
print(student["Age"])



# C. Dictionary Methods :
student = {
    1 : "Class - X",
    "Name" : "Nikhil",
    "Grade" : 'O',
    "City" : "Kadi"
}

print(student.keys())   # prints all keys
print(student.values())   # prints all values
print(student.items())   # prints both key and values

print(student["Name"])
print(student.get("Grade"))
print(student.get("Email", "Nahi Hai"))



# D. Add/Modify items in dictionary
student = {
    1 : "Class - X",
    "Name" : "Nikhil",
    "Grade" : 'O',
    "City" : "Kadi"
}

# Add item
student["Email"] = "nikhilparmarofc@gamil.com"
print(student)

# modify/replace item 
student["Grade"] = "O+"
print(student)

# remove items
del student["Grade"]
print(student)

# pop method
var1 = student.pop("Email")
print(var1)
print(student)




# E. Dictonary Loop Iteration
student = {
    1 : "Class - X",
    "Name" : "Nikhil",
    "Grade" : 'O',
    "City" : "Kadi"
}

for keys in student :   # for keys only
    print(keys)

for value in student :  # for values only
    print(student[value])

for key, value  in student.items() :    # For both
    print(key," : ", value)




# F. Nested Dictionary
students = {
    'student1' : {"Name" : "Nikhil", "Age" : 17},
    'student2' : {"Name" : "Prem", "Age" : 18, "Grade" : 'A'}
}

print(students)
print(students["student1"])
print(students["student1"]["Name"])
print(students["student2"]["Age"])



# G. Disctionary Comprehention
new_dict = {x: x+x for x in range(1, 6)}
print(new_dict)