# Write a program to show Explicit type casting in Python.
# Date: 09/01/2026
# Author: Nikhil


# In programer need to manually convert data type


# 1. Integer to Float
a = 10
print(a)
print(type(a))

a1 = float(a)
print(a1 + 1.2)
print(type(a1))


# 2. Integer to String
b = 18
print(b)
print(type(b))

b1 = str(b)
print(b1 + "19")
print(type(b1))


# 3. Float to Integer
c = 11.43
print(c)
print(type(c))

c1 = int(c)
print(c1)
print(type(c1))


# 4. Float to String
d = 12.67
print(d)
print(type(d))

d1 = str(d)
print(d1 + "Nikhil")
print(type(d1))

# 5. String to Integer
e = "213"
print(e)
print(type(e))

e1 = int(e)
print(e1 + 2)
print(type(e1))

# e2 = "Nikhil"
# print(int(e2))  # this shows error because every string can't be converted to integer


# 6. String to float
f = "6253.32"
print(f)
print(type(f))

f1 = float(f)
print(f1 + 2.2)
print(type(f1))
