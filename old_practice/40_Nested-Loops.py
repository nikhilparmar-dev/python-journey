# WAP to show the use of Nested Loops in python.
# Date: 17/02/2026
# Author: Nikhil

# 1 : print numbers from 1 to 3 for 3 times (for loop) 
for i in range (3) :
    print("Outer loop iteration: ", i+1)
    for j in range(1, 4) :
        print(j)
print("-----")


# 2 : print numbers from 1 to 3 for 3 times (while-for loop) 
i = 1 
while i < 4 :
    print("Outer Loop Iteration: ", i)
    for j in range(1, 4) :
        print(j)
    print("-----")

    i += 1


# 3. print prime numbers between range of 2 to 10 using nested loop
for num in range(2, 10) :
    for i in range (2, num) :
        if num % i == 0  :
            break
    else :
        print(num)


# 4. Basic Nested Loop (Numbers)
for i in range(1, 4) :
    print("Outer loop: ", i)
    for j in range (1, 4) :
        print(i, j)


# 5. Star Pattern (Most Important)
for i in range(1, 6) :
    for j in range(i) :
        print("*", end=" ")
    print()

# num = int(input("Enter Number of Row: "))
# for i in range(1, num+1) :
#     for j in range(i):
#         print("*", end=" ")
#     print()



# 6. Number Pattern
for i in range(1, 6) :
    for j in range(1, i+1) :
        print(j, end=" ")
    print()



# 7. Square Star Pattern
for i in range(5) :
    for j in range(5) :
        print("*", end=" ")
    print()



# 8. Pyramid Star Pattern
for i in range(1, 6) :
    for space in range (5 - i) :
        print(" ", end="")
    for space in range (2*i - 1) :
        print("*", end="")
    print()



# 9. Inverted Triangle Star
for i in range(5, 0, -1) :
    for j in range(i) :
        print("*", end=" ")
    print() 



# 10. Same Number Pattern
for i in range(1, 6) :
    for j in range(i) :
        print(i, end=" ")
    print()



# 11. Alphabet Triangle
for i in range(1, 6) :
    ch = 65
    for j in range(i) :
        print(chr(ch), end=" ")
        ch += 1
    print()



# 12. Multiplication Tables (1 to 3)
for i in range(1, 4) :
    print(f"\nTable of {i}: ")
    for j in range (1, 11) :
        print(f"{i} x {j} = {i*j}")

    print("------------")