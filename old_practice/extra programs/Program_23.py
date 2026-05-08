# Write a Python Program to Display Fibonacci Sequence Using Recursion.
# Date : 18/02/2026
# Author : Nikhil

def rec_fibo (n) :
    if n <= 1 :
        return n
    
    else :
        return (rec_fibo(n-1) + rec_fibo(n-2))
    
nterms = int(input("Enter The Number of terms (greater than 0) : "))

if nterms <= 0 :
    print("Please enter a positive integer.")

else :
    print("Fiboncci sequence: ")
    for i in range(nterms) :
        print(rec_fibo(i))