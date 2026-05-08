# Write a Python program to find N largest elements from a list.
# Date : 19/02/2026
# Author : Nikhil

def find_n_largest_element (lst, n) :
    sorted_lst = sorted(lst, reverse=True) 

    largest_element = sorted_lst[:n]

    return largest_element

numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]

N = int(input("Enter N = "))

result = find_n_largest_element(numbers, N) 

print(f"The {N} largest elements in the list are: ", result)