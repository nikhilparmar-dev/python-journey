# Write a Python Program to Find the Sum of Natural Numbers.
# Date : 17/02/2026
# Author : Nikhil

limit = int(input("Enter the limit: "))

sum = 0

for i in range (1, limit+1) :
    sum += i
    
print(f"the sum of natural numbers upto {limit} is : {sum}")