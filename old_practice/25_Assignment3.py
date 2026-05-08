# Solve the assignment 2 of python.
# Date: 29/01/2026
# Author: Nikhil

# Q1: Leap Year: Write a simple program to 
# determine if a given year is a leap year 
# using user input.
# leap year condition: 
# 4 divisible & 100 not divisible 
# 400 divisible

year = int(input("Enter the Year: "))
if (year%4==0 and year%100!=0) or (year%400==0) :
    print("Leap Year")
else :
    print("Not leap year")


# Q2: Login Authentication using conditional statement. 
# Assume you have a predefined username and password. 
# Write a program that prompts the user to enter a username and password and checks whether they match. 
# Provide appropriate messages for the following cases:
# Both username and password are correct.
# Username is correct but password is incorrect.
# Username is incorrect.

# pre_user = "Nikhil"
# pre_pass = 1821

# user = input("Enter Username: ")
# Pass = int(input("Enter Password: "))
# if user == pre_user :
#     if Pass == pre_pass :
#         print("Login sucess")
#     else :
#         print("Password incorect!")
# else :
#     print("Username is incorrect!")



# Q3: Admission Eligibility: A university has the following 
# eligibility criteria for admission:
# Marks in Mathematics >= 65
# Marks in Physics >= 55
# Marks in Chemistry >= 50
# Total marks in all three subjects >= 180 OR- 
# -Total marks in Mathematics and Physics >= 140
# Write a program that takes marks in three subjects as input and prints whether the student is eligible for admission.

# print("Enter Your subject Marks out of 100\n")
# phy = int(input("Enter Your Physics marks: "))
# chem = int(input("Enter Your chamestry marks: "))
# math = int(input("Enter your mathematics marks: "))

# if (phy >= 55 and chem >= 50 and math >= 65) and (((phy+chem+math) >= 180) or (math+phy) >= 140) :
#     print("Eligible for addmission")
# else :
#     print("Not eligible!")