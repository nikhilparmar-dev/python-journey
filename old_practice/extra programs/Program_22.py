# Write a Python Program to Make a Simple Calculator with 4 basic mathematical
# operations.
# Date : 17/02/2026
# Author : Nikhil

def add(x, y) :
    return x+y

def sub(x, y) :
    return x-y

def mult(x, y) :
    return x*y

def div(x, y) :
    return x/y


print("Select Operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True :
    choice = input("Enter Choice (1/2/3/4) : ")

    if choice in ('1', '2', '3', '4') :
        try :
            num1 = float(input("Enter the First Number: "))
            num2 = float(input("Enter the Second Number: "))
        except ValueError :
            print("Invalid Input! Please enter a number.")
            continue

        if choice == '1' :
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2' :
            print(f"{num1} - {num2} = {sub(num1, num2)}")

        elif choice == '3' :
            print(f"{num1} x {num2} = {mult(num1, num2)}")

        elif choice == '4' :
            print(f"{num1} / {num2} = {div(num1, num2)}")


        nextCalculation = input("Let's do next calculation? (yes/no) : ")
        if nextCalculation == "no" :
            break

    else :
        print("Invalid Input")