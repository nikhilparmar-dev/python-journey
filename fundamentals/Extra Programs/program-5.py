#  Program 5 — Dictionary Operations

""" Create a dict for a student:
name, age, marks (list of 5), city

Write functions:
- get_average(student) → returns average marks
- get_grade(student) → returns grade based on average
- print_report(student) → prints full report card

Call all 3 functions """

name = input("Enter Your name: ")
age = int(input("Enter Your Age: "))

Marks = []
for i in range(5) :
	Mark = int(input(f"Enter Subject {i+1} Marks : "))
	Marks.append(Mark)
	
city = input("Enter Your city: ")
	
student = {
"name" : name,
"age" : age,
"marks" : Marks,
"city" : city
}


# Function 1 :
def get_average(student) :
	sum = 0
	
	for mark in student.get("marks") :
		sum += mark
		
	return sum / len(student.get("marks"))
	
	
	
# Function 2 :
def get_grade(student) :
	avg = get_average(student)
	
	if 90 <= avg <= 100 :
		print("GRADE : A+")
		
	elif 80 <= avg <= 89 :
		print("GRADE : A")
		
	elif 70 <= avg <= 79 :
		print("GRADE : B")
		
	elif 60 <= avg <= 69 :
		print("GRADE : C")
		
	elif avg <= 59 :
		print("FAIL")
		
	else :
		print("Invalid Marks Entered")
		
		

# Function 3 :		
def print_report(student) :
	
	print("\nFULL STUDENT CARD: ")
	for key, value in student.items() :
		
		print(f"{key} : {value}")
		
		
		
get_average(student)
print_report(student)
get_grade(student)