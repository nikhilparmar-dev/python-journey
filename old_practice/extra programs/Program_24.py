# Write a Python Program to Find Factorial of Number Using Recursion.
# Date : 18/02/2026
# Author : Nikhil

def rec_fac(n) :
    if n == 1 :
        return n
    else :
        return n * rec_fac(n-1)
    

num = int(input("Enter the number: "))

if num < 0 :
    print("Sorry! factorial does not exist for negative numbers")

elif num == 0 :
    print("The factorial of 0 is 1.")

else :
    print(f"The factorial of {num} is {rec_fac(num)}")