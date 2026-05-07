# Create a student profile using all 7 data types Then print each value with a label.

name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
per = float(input("Enter Percentage: "))
city = input("Enter City: ")
pin = int(input("Enter Your Pincode: "))
state = input("Enter Your state: ")

is_Passed = False

if per >= 33 :
	is_Passed = True
	
Subjects = ["C", "DBMS", "Python", "C++", "Java"]

address = {
"City" : city,
"Pincode" : pin,
"State" : state
}

print("\nStudent Details: ")
print("--------------------")
print("Name: ", name)
print("Age: ", age)
print("Percentage: ", per, "%")

if is_Passed :
	print("Result : Pass")
else :
	print("Result : Fail")
	
print("Subjects: ", Subjects)
print("Address: ", address)
