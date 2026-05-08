# WAP to show the use of operators in python.
# Date: 20/01/2026
# Author: Nikhil

# 1. Arithmetic operator :
print("\n- Arithmetic Operators")
a = 5
b = 3
print(a+b)  #addition
print(a-b)  #subtraction
print(a*b)  #multiplication
print(a/b)  #division
print(a%b)  #multiplication
print(a//b) #floor

# 2. Comarision (Relational operators)
print("\n\n- Comparision operators")
a = 5
b = 7
print(a==b) #is equal to
print(a!=b) #not equal to
print(a>b)  #greater than
print(a<b)  #less than
print(a<=b) #less than equal to
print(a>=b) #greater than equal to


# 3. Assignment Operators
print("\n\n- Assignment operators")
a = 5
b = a
print(b)
print(a)

# 4. Logical Operators
print("\n\n- Logical operators")
a = 10
b = 10
c = 15
print(a==10 and b==10)
print(a!=10 and b!=10)
print(a>b or a<b)
print(not (a<=c or c>=b))
print(not(a==b and c==b))

# 5. Identity Operators - is, is not
print("\n\n- Ideentity operators")
x = [18, 6, 2008]
y = x
z = [18, 6, 2008]
print(y is x)
print(z is y)
print(z is not y)
print(x is not y)


# 6. Membership Operators - in, not in
print("\n\n- Membership operators")
fruits = ['apple', 'mango', 'banana']
print('mango' in fruits)
print('orange' in fruits)
print('orange' not in fruits)


# 7. Bitwise Operators 
print("\n\n- Bitwise operators")
a = 5
b = 3
print(a & b)    #AND
print(a | b)    #OR
print(a ^ b)    #XOR

# RULES FOR AND (&)
# 1. TRUE + TRUE = TRUE
# 2. TRUE + FALSE = FALSE
# 3. FALSE + TRUE = FALSE
# 4. FALSE + FALSE = FALSE

# RULES FOR OR (|)
# 1. TRUE + TRUE = TRUE
# 2. TRUE + FALSE = TRUE
# 3. FALSE + TRUE = TRUE
# 4. FALSE + FALSE = FALSE