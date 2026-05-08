# Write a Python Program for cube sum of first n natural numbers.
# Date : 18/02/2026
# Author : Nikhil

def cube_sum_of_natuaral_numbers (n) :
    if n <= 0 :
        return 0
    
    else :
        total = sum([i**3 for i in range(1, n+1)])
        return total
    
n = int(input("Enter the value of n: "))

if n <= 0 :
    print("Please enter a positive integer")

else :
    result = cube_sum_of_natuaral_numbers(n)
    print(f"The cube of first {n} natural numbers is {result}")