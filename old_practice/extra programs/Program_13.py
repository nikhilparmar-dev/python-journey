# Write a Python program to check if the given number is Happy Number.
# Date : 14/02/2026
# Author : Nikhil

def isHappyNumber(num) :
    seen = set()

    while num != 1 and num not in seen :
        seen.add(num)
        num = sum(int(i) ** 2 for i in str(num))

    return num == 1

num = int(input("Enter a number : "))

if isHappyNumber(num) :
    print(f"{num} is a Happy Number")
else :
    print(f"{num} is a not a Happy Number")