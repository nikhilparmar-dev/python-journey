# Write a Python Program to Find LCM
# Date : 12/02/2026
# Author : Nikhil

def computeLcm(x, y) :
    if x > y :
        greater = x
    else :
        greater = y

    while (True) :
        if ((greater % x == 0) and (greater % y == 0))  :
            lcm = greater
            break
        greater += 1

    return lcm

num1 = int(input("Enter a Number: "))
num2 = int(input("Enter a Number: "))

print("The L.M.C. is = ", computeLcm(num1, num2))