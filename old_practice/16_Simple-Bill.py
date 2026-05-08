# WAP to take input from user and find Simple Bill.
# Date: 17/01/2026
# Author: Nikhil

item = input("Enter Item Name: ")
price = int(input("Enter per 1 item price: "))
qun = int(input("Enter Quantity: "))

bill = price * qun

print(f"Your Final Bill for {item} is {bill}Rs.")