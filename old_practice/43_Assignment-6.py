# Solve the assignment 6 of python.
# Date: 23/02/2026
# Author: Nikhil

# 1. Print All Elements of a List
list = [10, 20, 30, 40, 50]

for num in list :
    print(num)



# 2. Find Sum of List Elements
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sum = 0

for num in list :
    sum += num
print("Sum of all elements: ", sum)



# 3. Find Largest Number in List
list = [18, 7, 45, 10, 33, 23]
max = list[0]

for num in list :
    if max < num :
        max = num
print("Largest element: ", max)



# 4. Find Smallest Number in List
list = [18, 7, 45, 10, 33, 23]
min = list[0]

for num in list :
    if min > num :
        min = num
print("Smallest element: ", min)



# 5. Count Even and Odd Numbers
list = [1, 2, 3, 4, 5, 6]
even = 0
odd = 0

for num in list :
    if num % 2 == 0 :
        even += 1
    else :
        odd += 1
print("Even numbers: ", even)
print("Odd numbers: ", odd)



# 6. Take List Input from User
numbers = []

n = int(input("How many numbers want to add ? : "))

for i in range(n) :
    num = int(input(f"Enter Number {i+1}: "))
    numbers.append(num)

print("List = ", numbers)
