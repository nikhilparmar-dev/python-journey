# Solve the assignment 7 of python.
# Date: 05/03/2026
# Author: Nikhil


# Q-1 : Student Information System
student = {
    "Name" : "Nikhil",
    "Course" : "BCA",
    "Fees" : 32000,
    "City" : "Kadi"
}

print("Name: ", student["Name"])
print("Course: ", student["Course"])



# Q-2 : Computer Institute Students System
students = {
    101 : "Nikhil",
    102 : "Prem",
    103 : "Zeeshan"
}
print("102 : ", students[102])



# Q-3 : Shopping Cart System
Cart = {
    "Pen" : 10,
    "Book" : 60,
    "Bag" : 300
}

total = sum(Cart.values())
print("Total Bill: ", total)



# Q-4 : Student Result System  
Marks = {
    "Physics" : 87,
    "Chemestry" : 74,
    "Mathematics" : 94
}

for subject, score in Marks.items() :
    print(subject, " : ", score)