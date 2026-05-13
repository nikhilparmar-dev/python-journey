# Program 10 — Mini Student System (Combine Everything)

"""
Build a complete system:

1. Class Student:
   - name, age, marks (list)
   - average() method
   - grade() method
   - __str__() method

2. Functions:
   - add_student(students_list) → takes input, creates Student, adds to list
   - show_all(students_list) → prints all students
   - save_to_file(students_list) → saves all to "class_data.txt"
   - find_topper(students_list) → returns student with highest average
   """
   
class Student :
	
	def __init__(self, name, age, marks):
		self.name = name
		self.age = age
		self.marks = marks
	
	
	def average(self) :
		
		avg = sum(self.marks) / len(self.marks)
		
		return avg
	
	def grade(self) :
	  	
	  	if 90 <= self.average() <= 100 :
	  		return "A+"
	  	
	  	elif 80 <= self.average() < 90 :
	  		return "A"
		
	  	elif 70 <= self.average() < 80 :
	  		return "B"
			
	  	elif 60 <= self.average() < 70 :
	  		return "C"
			
	  	elif self.average() < 60 :
	  		return "FAIL"
		
	  	else :
	  		return "Invalid Marks Entered"
   	
	def __str__ (self) :
	  	return f"""
	  	Name : {self.name}
	  	Age : {self.age}
	  	Marks : {self.marks}
	  	Average : {self.average():.2f}
	  	Grade : {self.grade()}
	  	"""
	  		  	
   	
   	
   	
def add_student():

	student_list = []

	n = int(input("\nHow many Students Data want to enter?: "))
	sub = int(input("How Many Subjects you have?: "))

	for i in range(n):

		print(f"\nEnter Student {i+1} Details: ")

		name = input("Enter Name: ")
		age = int(input("Enter Age: "))

		marks = []

		for j in range(sub):

			m = int(input(f"Enter Subject {j+1} Marks: "))
			marks.append(m)
		
		s = Student(name, age, marks)

		student_list.append(s)
		
	print("\nStudents Data Added ✓")
	
	return student_list
		
		
		

def show_all(students_list) :
	
	print("\nAll Students : ")
	
	for student in students_list :
		print(student)
	
	
	
	
def save_to_file(students_list):

	with open("class_data.txt", "a") as file:

		for student in students_list:
			file.write(str(student) + "\n")
		
		print("\nData saved as file ✓")
		
		
		
def find_topper(students_list):

	topper = students_list[0]

	for student in students_list:

		if student.average() > topper.average():
			topper = student

	print("\nTopper Student : ")
	print(topper)
				


"""
3. Main program   
"""
choice = 0
students_list = []

while choice != 5 :
	
	print("\nSTUDENT MANAGEMENT")
	
	print("\nMenu : ")
	print("1. Add Students")
	print("2. Show all students")
	print("3. Print topper")
	print("4. Save to file")
	print("5. Exit")
	
	choice = int(input("\nEnter choice : "))
	
	if choice == 1 :
		students_list.extend(add_student())
		
	elif choice == 2 :
		if not students_list:
			print("No Students Added")
		else:
			show_all(students_list)
		
	elif choice == 3 :
		if not students_list:
			print("No Students Added")
		else:
			find_topper(students_list)
		
	elif choice == 4 :
		if not students_list:
			print("No Students Added")
		else:
			save_to_file(students_list)
				
	elif choice == 5 :
		print("\nThank You")
		break
		
	else :
		print("\nInvalid choice")