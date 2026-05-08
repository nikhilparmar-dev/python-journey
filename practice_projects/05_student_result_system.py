# Mini Project #5 -  Student Marks Result System (Loops)
# Date: 16/02/2026
# Author: Nikhil


total = 0

subjects = int(input("Enter number of subjects: "))

for i in range(1, subjects + 1) :

    marks = int(input(f"Enter marks for Subject {i}: "))
    total += marks

average = total / subjects

print("Total Marks: ", total)
print("Percentage: ", average)