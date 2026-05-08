# WAP to show the use of While Loop in python.
# Date: 12/02/2026
# Author: Nikhil

# 1. 1 to 5
count = 1
while count <= 5 :
    print(count)
    count += 1


# 2. 5 to 1
count = 5
while count >= 1 :
    print(count)
    count -= 1


# 3. Print 10 Even Numbers 
count = 2
while count <= 10 :
    print(count)
    count += 2


# 4. Print Table of a number
# i = 1
# no = int(input("Enter an Number: "))
# while i <= 10 :
#     print(f"{no} * {i} = {no*i}")
#     i += 1 



# 5. Count Number of Digits
num = int(input("Enter a Number: "))
count = 0

while num != 0 :
    num = num // 10
    count += 1

print("Total Digit = ", count)