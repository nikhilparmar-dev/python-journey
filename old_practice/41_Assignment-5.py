# Solve the assignment 5 of python.
# Date: 19/02/2026
# Author: Nikhil

# 1: print in the same line.
print("Hello", "Madhav1", sep="*", end=" * ")
print("Madhav")


# while loop to print the output in the same line
i = 1
while i < 4 :
    print(f"Hello madhav {i}", end=" ") 
    i += 1

i = 1
while i < 4 :
    print(f"Hello{i}", "Madhav", sep="*", end=" ")
    i += 1


# 2: Loop Patterns.

# a.
n = 5
for i in range(1, n+1) :
    for j in range(1, i+1) :
        print("*", end=" ")
    print()

for i in range(1, n+1) :
    print("* " * i)

# b. 
n = 5
for i in range(n, 0, -1) :
    for j in range(1, i+1) :
        print("*", end=" ")
    print()

for i in range(n, 0, -1) :
    print("* " * i)

# c.
n = 5
for i in range(1, n+1) :
    print(' ' * (n-i), end="")
    print("*" * (2*i-1))

for i in range(1, n+1) :
    print(' ' * (n-i) + "*" * (2 * i - 1))



# 3: Factorial of a number.
def fact(n) :
    result = 1
    while n > 0 :
        result *= n
        n -= 1
    return result

print(fact(5))



# 4: Count vowels in a string.
my_string = "python by nikhil parmar"
vowels = "aeiou"
count = 0

for char in my_string :
    if char.lower() in vowels :
        count += 1
print("Number of vowels are: ", count)



# 5: Longest word in a string 
sentence = "python by nikhil parmar"
words = sentence.split()
longetWord = ""

for word in words :
    if len(word) > len(longetWord) :
        longetWord = word
print("Longets word is: ", longetWord)




# 6: do-while loop in python 
# while True :
#     num = int(input("Enter number greather than 10: "))

#     if num > 10 :
#         print("Valid number entered: ", num)
#         break
#     else : 
#         print("Number is not greather than 10, try agin !")




# 7. Fibonacci Sequence 

def fibonacci(n) :
    a, b = 0, 1
    count = 0

    while count < n :
        print(a)
        a, b = b, a+b
        count += 1

fibonacci(10)