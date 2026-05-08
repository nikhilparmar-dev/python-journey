# Write a Python Program to Find the Factorial of a Number.
# Date : 16/02/2026
# Author : Nikhil

num = int(input("Enter a Number: "))

factorial = 1

if num < 0 :
    print("factorial does not exist for negative numbers.")

elif num == 0 :
    print("Factorial for 0 is 1")

else :
    for i in range(1, num+1) :
        factorial = factorial * i

    print(f"Factorial of {num} is: {factorial}")