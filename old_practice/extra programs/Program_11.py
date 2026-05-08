# Write a Python Program to Check Armstrong Number?
# Date : 12/02/2026
# Author : Nikhil

num = int(input("Enter a Number: "))

numStr = str(num)
numDigits = len(numStr)

sumOfPowers = 0
tempNum = num

while tempNum > 0 :
    digit = tempNum % 10
    sumOfPowers += digit ** numDigits
    tempNum //= 10

if sumOfPowers == num :
    print(f"{num} is a armstrong number!")
else :
    print(f"{num} is not an armstrong number!")