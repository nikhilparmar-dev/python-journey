# Write a program to show Data Types in Python.
# Date: 09/01/2026
# Author: Nikhil

a=1
b=2
print(a+b)
print(type(a)) # Checking data type using type function

# I. Integer data type
c=10
d=-20
print(d)
print(type(d))

# II. Float data type
e = 18.45
f = 7
print(e+f)
print(type(e))

# III. String data type
g = "Hello"
h = " World"
print(g+h)
print(type(g))
 # Another way to use string data type
i = 'n'
j = 'p'
print(i+j)
print(type(i))



# Basic Data Types in Python
#----------------------------

# 1. Numeric
a1 = 10 #Integer
a2 = 4.2 #Float
print(type(a2))
a3 = complex(5, 4) #Complex
print(a3)
print(type(a3))

# 2. Sequence
b1 = "Nikhil" #String
b2 = "1234" #String
print(type(b1))
c1 = [12, 23, 34, 45, 'Nikhil'] #List
print(c1)
print(type(c1))
c2 = (18, 23, 1, 3, "Green", 'red', "Blue") #tuple
print(c2)
print(type(c2))

# 3. Dictionary
info = {'Name':'Nikhil', 'age': 17, 'city' : 'kadi'}
print(info)
print(type(info))
student = {
    'Name' : 'Zeeshan',
    'Age' : 19,
    'Percentage' : 75.82
}
print(student)
print(type(student))


# 4. Sets
my_sets = {1, 2, 3, 4, "Nik", 'BCA'}
numbers = {18, 45, 7, 10, 33}
print(my_sets)
print(numbers)
print(type(my_sets))
print(type(numbers))


# 5. Boolean
isStudent = True
isTeacher = False
print(isStudent)
print(type(isStudent))


# 6. Binary

data = b'ABC'   #Bytes type
print(data)
print(type(data))

data2 = bytearray([2, 1, 5])    #Bytearray
data2[0] = 15
print(data2)
print(type(data2))

data3 = bytearray(b'Nikhil')    #Memory View
view = memoryview(data3)
print(view[0])
print(type(view))