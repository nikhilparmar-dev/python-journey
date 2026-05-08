# Write a Python program to sort Python Dictionaries by Key or Value.
# Date : 07/03/2026
# Author : Nikhil


sample_dict = {'apple' : 3, 'banana' : 1, 'cherry' : 2, 'date' : 4}


shorted_dict_by_keys = dict(sorted(sample_dict.items()))

print("Shorted By keys: ")

for key, value in shorted_dict_by_keys.items() :
    print(f"{key}: {value}")