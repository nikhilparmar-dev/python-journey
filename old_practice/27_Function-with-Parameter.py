# WAP to show the use of Function with parameter in python.
# Date: 29/01/2026
# Author: Nikhil


# 1.
def printName(name) :
    print("Name: ", name)
printName("Nikhil")


# 2.
def Addition(a, b) :
    print("Addition: ", a+b)
Addition(5,6)


#3.
def Square(num) :
    print("Square= ", num * num)
Square(4)


#4. 
def EvenOddCheck(num) :
    if num % 2 == 0 :
        print("Even Number")
    else :
        print("Odd Number")
EvenOddCheck(7)


#5.
def Result(marks) :
    if marks >= 33 :
        print("PASS")
    else :
        print("FAIL")
Result(67)


# 6. 
def Voting(age) :
    if age >= 18 :
        print("Eligible for vote")
    else :
        print("Not eligible for vote")
Voting(17)


# 7. 
def largest(num1, num2) :
    if num1 > num2 :
        print(f"{num1} is greater")
    else :
        print(f"{num2} is greater")
largest(45, 18)


#8. simple interest
def SI(p, r, t) :
    print("Simple interest = ", p*r*t/100)
SI(1000, 5, 2)


# 9. grade system
def Showresult(marks) :
    if marks > 90 :
        print("A Grade")
    elif marks > 80 :
        print("B grade")
    else :
        print("C grade")
Showresult(68)


# 10.
def Greet(time) :
    if time < 12 :
        print("Good Morning")
    elif time < 16 :
        print("Good Afternoon")
    elif time < 20 :
        print("Good Evening")
    else :
        print("Good Night")
Greet(16.5)


# 11. 
def addThree(a, b, c) :
    result = a + b + c
    print("Result = ", result)
addThree(b=15,a=12,c=3)
