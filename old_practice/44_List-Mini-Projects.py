# Write some list mini projects in python.
# Date: 23/02/2026
# Author: Nikhil


# 1. Shopping Cart System
cart = []

cart.append("Milk")
cart.append("Bread")
cart.append("Butter")

print("Your cart Items: ")
for item in cart :
    print(item)
print("------------------")
print("Total Items: ", len(cart))




# 2. Student Marks System
marks = [78, 85, 90, 68, 87, 99]

total = sum(marks)
percentage = total / len(marks)

print("Total Marks: ", total)
print("Percentage: ", percentage, "%")




# 3. Contact List
contacts = ["Prem", "Tushar", "Zesshan", "Nikhil"]

search = "Jaimin"

if search in contacts :
    print("Contact found!")
else :
    print("Contact not found!")




# 4. Bank Transaction History
transactions = [2000, -500, 1500, -700, 3000]

balance = 0

for amount in transactions :
    balance += amount

print("Final Balance: ", balance)




# 5. Attendance System
students = ["Nikhil", "Prem", "Zeeshan", "Tushar"]

present = ["Nikhil", "Prem"]

for name in students :
    if name in present :
        print(name, " - Present")
    else :
        print(name, " - Absent")




# 6. Restaurant Order System
menu = ["Pizza", "Burger", "Pasta", "Sabdwich"]
order = []

order.append("Pizza")
order.append("Pasta")

print("Ordered Items: ")
for item in order :
    print(item)




# 7. Inventory Management
stock = ["Pen", "Notebook", "Pencil", "Eraser"]

removeItem = "Pencil"

if removeItem in stock :
    stock.remove(removeItem)

print("Updated Stock: ", stock)