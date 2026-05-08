# Write a Python Program to Print the Fibonacci sequence
# Date : 12/02/2026
# Author : Nikhil

n_terms =  int(input("How Many Terms?: "))

n1, n2 = 0, 1
count = 0

if n_terms <= 0 :
    print("Please enter an positive number.")

elif n_terms == 1 :
    print("Fibonacci sequence upto ", n_terms, ": ")
    print(n1)

else :
    print("Fibonacci Sequence: ")
    while count < n_terms :
        print(n1)
        nth = n1 + n2

        n1 = n2
        n2 = nth
        count += 1