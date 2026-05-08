# WAP to show the use of Lists in python.
# Date: 21/02/2026
# Author: Nikhil


# 1. create list
list1 = [1, 2, 3]
print(list1)

list2 = ["Nikhil", "prem", "zeeshan", "Tushar"]
print(list2)
print(type(list2))

list3 = [18, "nikhil", 9.00,  5, "Prem", 8.99]
print(list3)
print(type(list3))


# 2. Access List (Indexing)
list = [10, 20, 30, 40, 50]

print(list[0])  # First element
print(list[1])  # second element
print(list[-1])  # last element
print(list[-2])  # second last element



# 3. List slicing
list2 = [10, 20, 30, 40, 50, 60, 100]

print(list2[0:3:1])     # first 3 elements
print(list2[-3::1])     # last 3 elements
print(list2[::2])     # alternative elements
print(list2[::-1])     # reverse list




# 4. List modify
my_list = ["Apple", "Banana", "Cherry"]

print(my_list)

my_list[1] = "BlueBarry"    # Replece element at index 1
print(my_list)

my_list.append("Mango")    # add element in list
print(my_list)

my_list.remove("Cherry")    # remove element from the list
print(my_list)




# 5. List Methods

# a. append :
fruits = ["Apple", "Banana", "Orange"]
fruits.append("Cherry")
fruits.append(108)
print(fruits)

# b. extend :
fruits = ["Apple", "Orange"]
moreFruits = ["Cherry", "Mango"]    # another list
fruits.extend(moreFruits)
print(fruits)

# c. insert : 
fruits = ["Apple", "Orange"]
fruits.insert(1, "Blueberry")
print(fruits)

# d. remove : 
fruits = ["Apple", "Banana", "Orange", "Banana"]
fruits.remove("Banana")
print(fruits)

# e. clear : 
fruits = ["Apple", "Orange"]
fruits.clear()  # empty list
print(fruits)

# f. finding index : 
fruits = ["Apple", "Banana", "Cherry", "Banana"]
index = fruits.index("Banana")
print(index)

index = fruits.index("Banana", 3)  # WIthin range
print(index)

# g. count elements : 
fruits = ["Apple", "Banana", "Cherry", "Banana"]
index = fruits.count("Banana")
print(index)

# h. Reverse List :
fruits = ["Apple", "Banana", "Cherry", "Banana"]
fruits.reverse()
print(fruits)

# i. shorting list :
numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)  #decending order
print(numbers)

fruits = ["cherry", "apple", "banana", 'blueberry']     #sorting string list
fruits.sort()   # based on characters
print(fruits)

fruits.sort(key=len, reverse=True)   # based on length & in reverse order
print(fruits)

# j. pop with index value :
numbers = [10, 20, 30, 40]
popped = numbers.pop(2)
print(popped)
print(numbers)

last = numbers.pop()    # with default value
print(last)
print(numbers)

# k. copying list :
fruits = ["Apple", "Banana", "Cherry"]
copyFruits = fruits.copy()
print(copyFruits)

copyFruits.append("Mango")
print(copyFruits)
print(fruits)




# 6. Join Lists

lsit1 = [1, 2, 3]
list2 = ['a', 'b']

final_list = list1 + list2  # using + operator
print(final_list)

for x in list2 :    # using append method
    list1.append(x)
print(list1)

list1.extend(list2) # using extend method
print(list1)




# 7. List comprehensions 
squares = [x**2 for x in range(1, 5)]
print(squares)

even_list = [x for x in range(1, 20) if x % 2 == 0]
print(even_list)

fruits = ["Apple", "Mango", "Cherry"]
print(fruits)
upperList = [lst.upper() for lst in fruits]
print(upperList)

nested_List = [[1, 2], [3, 4], [5, 6]]
result = [item for sublist in nested_List for item in sublist]
print(result)




# 8. List iterations
fruits = ['apple', 'mango', 'cherry']

# a. using for loop
for fruit in fruits :
    print(fruit)
print("lenght of list: ", len(fruits))

# b. using while loop
index = 0
while index < len(fruits) :
    print(fruits[index])
    index += 1




# 9. List function examples :
list1 = [1, 9, 11]

print(len(list1))   # Find length of list
print(min(list1))   # Find minimum value in the list
print(max(list1))   # Find maximum value in the list
print(sum(list1))   # Find sum of all list elements