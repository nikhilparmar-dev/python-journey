# Write a Python program to split and join a string.
# Date : 19/02/2026
# Author : Nikhil

input_str = "Python program to split and join a sting"
word_list = input_str.split()

separator = " "
output_str = separator.join(word_list)

print("Origional String: ", input_str)
print("Words split from the string: ", word_list)
print("joined string: ", output_str)