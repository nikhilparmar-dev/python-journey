# WAP to show the use of Function with Arguments in python.
# Date: 03/02/2026
# Author: Nikhil

# 1. Required Arguments (single/multiple arguments)
def greeting(name) :
    print("Good Morning, ", name, "!")
greeting("Nikhil")

def intro(courseName, InstituteName) :
    print("Welcome to ", courseName, " course By ", InstituteName)
intro("DIT", "Nutan Computer")


# 2. Default Arguments 
def greetings(name = "World") :
    print("Hello ", name, "!")
greetings()
greetings("NIK")


# 3. Keyword Arguments (named argument)
def devide(a, b) :
    return a/b

result1 = devide(10,5)
print(result1)

result2 = devide(b = 500, a = 25)
print(result2)


# 4. Arbitrary Argument
def showNumbers(*args) :
    print(args)

showNumbers(10, 20, 30, 40)
showNumbers(18, 45, 7, 33, 10)



# 5. # Arbitrary Keyword Argument (**kwargs)
def StudentInfo(**kwargs) :
    print(kwargs)

StudentInfo(
    Name = "Nikhil",
    age = 17,
    course = "BCA",
    SGPA = 9.00
)
#-------------
def Bill(**items) :
    total = items["pen"] + items["book"] + items["bag"]
    print("Total Bill: ", total)

Bill(
    pen = 5,
    book = 20,
    bag = 800
)
#-------------
def salary(**pay) :
    total = (pay["hra"] + pay["basic"] + pay["bonus"]) - pay["pf"]
    print("Final Salary: ", total)

salary(hra = 8000, basic = 8000, bonus = 2000, pf = 1500)


def login(**user) :
    print("Username: ", user["username"])
    print("Password: ", user["password"])

login(username = "Nikhil1234", password = 1234567890)
#--------------
def supermarketBill(billNo, **items) :
    print("======SUPERMARKET BILL=========")
    print("Bill No.: ", billNo)
    print("---------------------------------")
    print("Items")