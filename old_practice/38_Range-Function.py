# WAP to show the use of For Loop with range() function in python.
# Date: 14/02/2026
# Author: Nikhil

# 1. Print 0 to 5
for i in range(6) :
    print(i)


# 2. Print 5 to 10
for i in range(5, 11) :
    print(i)


# 3. Print 1 to 9 with 3 steps
for i in range(1, 10, 3) :
    print(i)


# 5. With Else Statement
for i in range(5) :
    print(i)
else :
    print("For Loop Ended")


# 6. Print Even Numbers from 1 to 20
for i in range(21) :
    if i % 2 == 0 :
        print(i)
    

# 7. Print Multiplication Table of a Number
# num = int(input("Enter a Number: "))

# for i in range(11) :
#     print(f"{num} x {i} = {num*i}")



# 8. Print Reverse Numbers from 10 to 1

for i in range(10, 0, -1) :
    print(i)


# 9. Find Factorial of a Number
# num = int(input("Enter an Number: "))

# fact = 1
# for i in range(1, num + 1) :
#     fact *= i

# print(f"Factorial of {num} is : {fact}")



# 10. Print Star Pattern
for i in range(1, 6) :
    print(" *" * i)