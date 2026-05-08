# Write a Python program to find largest number in a list..
# Date : 18/02/2026
# Author : Nikhil

numbers = [30, 10, -35, 5, 20]

maximum = numbers[0]

for i in numbers :
    if i > maximum :
        maximum = i


print("The largest number in the list is: ", maximum)