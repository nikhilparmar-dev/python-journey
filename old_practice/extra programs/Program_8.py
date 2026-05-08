# Write a Python program to show the use of function and show strong number checker.
# Date : 06/02/2026
# Author : Nikhil

def check_password(password):
    if len(password) >= 8:
        return "Strong Password"
    else:
        return "Weak Password"

pwd = input("Enter password: ")
print(check_password(pwd))
