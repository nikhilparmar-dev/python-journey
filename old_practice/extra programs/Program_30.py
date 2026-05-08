# Write a Python program to find smallest number in a list..
# Date : 18/02/2026
# Author : Nikhil

numbers = [30, 10, -35, 5, 20]

minimum = numbers[0]

for i in numbers :
    if i < minimum :
        minimum = i


print("The smallest number in the list is: ", minimum)