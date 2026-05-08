# Project : Mini Calculator.
# Date: 04/02/2026
# Author: Nikhil

# function to add numbers
def add(num1, num2) :
    return num1 + num2

# function to minus numbers
def sub(num1, num2) :
    return num1 - num2

# function to multiply numbers
def multiply(num1, num2) :
    return num1 * num2

# function to devide numbers
def devide(num1, num2) :
    return num1 / num2

# Function to average two numbers 
def avg(num1, num2) :
    return (num1+num2)/2

print("Please select an operation :\n" \
    "1. Addition\n" \
    "2. Subtraction\n" \
    "3. Multiplication\n" \
    "4. Division\n" \
    "5. Avarage")

select = int(input("Select a operation from 1,2,3,4,5: "))

num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second number: "))

if select == 1 :
    print(f"{num1} + {num2} = ", add(num1, num2))
elif select == 2 :
    print(f"{num1} - {num2} = ", sub(num1, num2))
elif select == 3 :
    print(f"{num1} * {num2} = ", multiply(num1, num2))
elif select == 4 :
    print(f"{num1} / {num2} = ", devide(num1, num2))
elif select == 5 :
    print(f"{num1} + {num2} / 2 = ", avg(num1, num2))
else :
    print("Invalid choice!")
