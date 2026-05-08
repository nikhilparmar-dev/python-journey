# Write a Python program to find the sum of all items in a dictionary.
# Date : 07/03/2026
# Author : Nikhil


my_dict = {
    'a' : 10,
    'b' : 20,
    'c' : 30,
    'd' : 40,
    'e' : 50
}

total_sum = 0


for i in my_dict.values() :
    total_sum += i

print("Sum of all values in dictionary: ", total_sum)