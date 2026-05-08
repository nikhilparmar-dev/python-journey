# Mini Project #2 - STUDENT ID CARD SYSTEM
# Date: 09/02/2026
# Author: Nikhil

print("\n---Enter Student Details: ---")

name = input("Enter Name: ")
course = input("Enter Course: ")
mobile = input("Enter Mobile No.: ")
year = input("Enter Addmission Year: ")

nameUpper = name.upper()

studentId = name[:2].upper() + year

email = name.replace(" ", "").lower() + "@nutanedu.com"

maskedMobile = mobile[:2] + "******" + mobile[-2:]

courseCode = course.split()[0][:3].upper()

print("\n======== GENERATED ID CARD ===========")
print("Name        : ", nameUpper)
print("Course ID   : ", studentId)
print("Course Code : ", courseCode)
print("Email       : ", email)
print("Mobile      : ", maskedMobile)