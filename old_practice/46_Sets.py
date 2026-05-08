# WAP to show the use of Sets in python.
# Date: 27/02/2026
# Author: Nikhil


# 1. Creating set using curly brackets
my_set = {1, 2, 3}
print(my_set)
print(type(my_set))



# 2. Creating set using set constructor
my_set2 = set([4, 5, 6])
print(my_set2)



# 3. Set Operations

# adding elements
numbers = {1, 2, 3, 4}
numbers.add(5)
print(numbers)

# removing elements
fruits = {"apple", "Mango", "Banana"}
fruits.remove("Banana")     # using remove
print(fruits)

fruits.discard("apple")     # using discard
print(fruits)



# 4. Set Methods

# a. Union (Cobine elements)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)

# b. Intersection (Common elemets)
set1 = {10, 20, 30}
set2 = {20, 50, 10, 80}
intersect_set = set1.intersection(set2)
print(intersect_set)

# c. Difference (element in first set but not in second)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)

# d. Symmetric difference (element in either set but not in bot)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
sd_set = set1.symmetric_difference(set2)
print(sd_set)

sd_set_2 = set1 ^ set2  # alternative
print(sd_set_2)



# 5. Set Iterations

numbers = {1, 2, 3, 4, 5}

for i in numbers :
    print(i)



# 6. Set Comprehentions

squares = {x**3 for x in range(1, 6)}
print(squares)