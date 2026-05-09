# Mini Project #9 - Student Shopping List Management System (Lists)
# Date: 25/02/2026
# Author: Nikhil

shopping_list = []
prices = []

def add_item() :

    item = input("Enter item name: ")
    price = float(input("Enter item price: "))

    shopping_list.append(item)
    prices.append(price)

    print(item, " Added Successfully!")


def remove_item() :

    item = input("Enter item name to remove: ")

    if item in shopping_list : 
        index = shopping_list.index(item)

        shopping_list.pop(index)
        prices.pop(index)
        print(item, " removed successfully")

    else :
        print("Item not found!")


def view_items() :

    if not shopping_list :
        print("Shopping list is empty")

    else :
        print("--- Shopping List ---")

        for i in range(len(shopping_list)) :
            print(f"{shopping_list[i]} - ₹{prices[i]}")


def total_bill() :

    total = sum(prices)
    print("Total Bill: ₹", total)



while True :

    print("\n=== Shopping Menu ===")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Items")
    print("4. Total Bill")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1 :
        add_item()

    elif choice == 2 :
        remove_item()

    elif choice == 3 :
        view_items()

    elif choice == 4 :
        total_bill()

    elif choice == 5 :
        print("Thank you for shopping")
        break

    else :
        print("Invalid choice!")