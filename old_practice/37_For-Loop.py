# WAP to show the use of For Loop in python.
# Date: 14/02/2026
# Author: Nikhil

# 1. normal printing
language = "Python" 
for x in language :
    print(x)


# 2. Printitems of list
numbers = [1, 2, 3, 4, 5]
for num in numbers :
    print(num)



# 3. Count Even Numbers in a List

numbers = [ 10, 15, 23, 34, 45, 14, 16, 13]
count = 0

for num in numbers :
    if num % 2 == 0 :
        count += 1
    
print('Total Even Numbers in a List :', count)


# 4. Find Sum of List Elements
numbers = [5, 10, 15, 20]
total = 0 

for num in numbers :
    total += num

print("Sum =", total)



# 5. Find Largest Number in a List
numbers = [12, 45, 7, 89, 23]
largest = numbers[0]

for num in numbers :
    if num > largest :
        largest = num

print("Largest Number in a List :", largest)



# 6. Count Vowels in a String
text = input("Enter the String: ")
count = 0

for char in text :
    if char.lower() in "aeiou" :
        count += 1

print("Total Wovels in string:", count)