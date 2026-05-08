# Write a Python Program to Find Armstrong Number in an Interval.
# Date : 17/02/2026
# Author : Nikhil

lower = int(input("Enter the lower limit of the interval: "))
upper = int(input("Enter the upper limit of the interval: "))

for num in range(lower, upper+1) :

    order = len(str(num)) 
    tempNum = num
    sum = 0

    while tempNum > 0 :
        digit = tempNum % 10
        sum += digit ** order
        tempNum //= 10

    # checks if 'num' is armstrong number
    if num == sum :
        print(num)