
# Simple Calculator With Functions

def add(a, b) :
    return f"\nAddition = {a + b}"

def sub(a, b) :
    return f"\nSubtraction = {a - b}"

def mult(a, b) :
    return f"\nMultiplication = {a * b}"

def div(a, b) :

    if b == 0 :
        return "Number cannot devided by zero"

    return f"\nDivision = {a / b}"



def calculator() :

    no1 = int(input("Enter The First Number: "))
    no2 = int(input("Enter The Second Number: "))

    choice = input("\nChoose an Operation (+, -, *, /): ")

    if choice == "+" :
        print(add(no1, no2))

    elif choice == "-" :
        print(sub(no1, no2))

    elif choice == "*" :
        print(mult(no1, no2))

    elif choice == "/" :
        print(div(no1, no2))

    else :
        print("Invalid Choice!")



calculator()