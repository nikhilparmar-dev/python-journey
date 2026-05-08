# WAP to take input from user and find Simple Interest.
# Date: 17/01/2026
# Author: Nikhil

p = int(input("Enter Principle Amount: "))
r = int(input("Enter rate of Interest: "))
n = int(input("Enter Total Years: "))

SI = (p*r*n)/100

print(f"Your Simple Interest is: {SI}")