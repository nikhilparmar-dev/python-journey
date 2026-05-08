# WAP to show the use of Function with return value in python.
# Date: 31/01/2026
# Author: Nikhil


# 1. sum of two num.
def sum(a, b) :
    return a + b
print("Sum of 10 & 15 is : ", sum(10,15))


# 2. calculate bill
def bill(price, quantity) :
    return price * quantity
print("Bill: ",bill(70, 3))


# 3. Welcome message
def Welcome() :
    return "Welcome to Python!"
print(Welcome())


# 4. Return as it is
def Number(no) :
    return no
print(Number(18))


# 5. Check Number is Positive Or not
def isPositive(no) :
    return no > 0
print(isPositive(9))


# 6. Return first character of a string
def returnFirst(name) :
    return name[0]
print(returnFirst("Nikhil"))


# 6. Return word length
def returnLength(word) :
    return len(word)
print(returnLength("Nikhil"))


# 7. return uppercase word
def returnUppercase(word) :
    return word.upper()
print(returnUppercase("nikhil"))


# 8. return true if age is adult 
def isAdult(age) :
    return age >= 18
print(isAdult(17))


# 9. Return full name 
def fullName(name) :
    return name 
print(fullName("Nikhil Parmar"))


# 10. Return fixed contact Number
def Contact() :
    return 8511177244
print(Contact())

