# WAP to show the use of Tuples in python.
# Date: 26/02/2026
# Author: Nikhil


# 1. Creating Tuple
mytuple = (1, 2, 3)
print(mytuple)
print(type(mytuple))

mytuple2 = (18, "Nikhil", 45.10, True)
print(mytuple2)



# 2. Tuple without parantheses
tuple1 = 1, 2, 3
print(tuple1)
print(type(tuple1))



# 3. Tuple Constructor
tuple2 = tuple((1, 5, 9))
print(type(tuple2))
print(tuple2)

list1 = [1, 2, 3]
tuple3 = tuple(list1)
print(tuple3)



# 4. creating a single element tuple
a = ("a", )
print(type(a))



# 5. acess tuple - indexing
fruits = ('Apple', 'Mango', 'Cherry')
print(fruits[0])
print(fruits[-1])



# 6. Tuple slicing
newTuple = (10, 20, 30, 40, 50)
print(newTuple[0::3])
print(newTuple[::-1])
print(newTuple[3:5:])




# 7. Tuple Operations
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b')

tuple3 = tuple1 + tuple2
print(tuple3)

tuple2 = (1, 2, 3) * 3  #repetative
print(tuple2)

tuple22 = (1, 2, 3)     
print(1 in tuple22)     # Checking element in the tuple



# 8. Tuple Iterations
fruits = ("Apple", "Mango", "Cherry")

for i in fruits :   # For loop
    print(i)


i = 0
while i < len(fruits) :   # While loop
    print(fruits[i])
    i += 1



# 9. Tuple Methods 
color = ("Blue", "Green", "Orange", "Blue", "Red")

print(color.count("Green"))     # count element
print(color.index("Blue"))      # finding index

numbers = (2, 3, 1, 4)
print(len(numbers)) # length
print(sum(numbers)) # total
print(min(numbers)) # smallest number
print(max(numbers)) # largest number

# Sorting
a = sorted(numbers)
numbers = tuple(a)
print(numbers)



# 10. Tuple Pack & Unpack
a = "Nikhil"
b = 18
c = "Software Engineer"

pack_tuple = a, b, c    # Packing
print(pack_tuple)

name, age, profession = pack_tuple      # Unpacking
print("Name is: ", name)
print("Age is: ", age)
print("Profession is: ", profession)



# 11. Tuple Modification
tuple_numbers = (10, 20, 30)

list_nums = list(tuple_numbers)
print(list_nums)

list_nums[0] = 100
print(list_nums)

tuple_numbers = tuple(list_nums)
print(tuple_numbers)