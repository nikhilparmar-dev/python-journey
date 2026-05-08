# Write a Python program to find second largest number in a list.
# Date : 18/02/2026
# Author : Nikhil

numbers = [30, 10, -35, 5, 20]

numbers.sort(reverse=True)

if len(numbers) >= 2:
    second_largest = numbers[1]
    print("Second largest number in a list: ", second_largest)

else :
    print("The list not contain any second largest number")