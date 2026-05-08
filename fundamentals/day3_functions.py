# Basic Functions 
from re import X


def greet() :
    print("Hello")
def wc() :
    print("Welcome")
greet()
wc()



# Function with parameters 
def hello(name) :
    print(f"Hello {name}")
hello("Nikhil")

def sum(a, b) :
    print(a+b)
sum(5, 5)



# Function with return
def add(a, b) :
    return a+b

print("Sum = ", add(2, 3))

def check_Age(age) :
    if age >= 18 :
        return "Adult"
    else :
        return "Minor"
print(check_Age(17))



# Default Parameters 
def greet2(name, city = "Kadi") :
    print(f"{name} from {city}")
greet2("Nikhil")
greet2("Prem", "Ahmedabad")



# Keyword arguments
def profile(name, age, city) :
    print(name, age, city)

# order dosen't matter
profile(age = 17, city = "Kadi", name = "Nikhil")



# args - multiple positional arguments
def nums(*num) :
    print(num)  # Saved as tuple
nums(1, 2, 3, 4, 5, 6, 7, 8)



# kwargs - multiple keyword arguments
def show_info(**details) :
    print(details)  # Saved as Dictionary
show_info(name = "Nikhil", age = 17, city = "Kadi")



# Lambada Fun. - One liner 
square = lambda x: x * x
print(square(5))
cube = lambda x: x*x*x
print(cube(5))
add = lambda a, b : a + b
print(add(5, 10))


# Function Returning Multiple Values 
def details(name, age, city) :
    return name, age, city
print(details("Nikhil", 17, "Kadi"))


# Nested Function 
def outer() :
    print("This is oputer Function")
    
    def inner() :
        print("This is inner Function")

    inner()

outer()



# Factorial Using Recursion :
def fact(n) :

    if n == 1 :
        return 1

    return n * fact(n-1) 

print(fact(5))