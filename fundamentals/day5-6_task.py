
# Student Record System using File + Exception Handling:
	
#------------------------------------

def save_students(name, age, city) :
	file = open("students.txt", "a")
	file.write(f"Name: {name} | Age: {age} | City: {city}\n")
	file.close()
	
#------------------------------------
		
def read_students() :
	i = 1
	try :
				file = open("students.txt", "r")
				content = file.readlines()
				
				for line in content :
					print(f"{i}. {line}", end="")
					i+=1
					
	except FileNotFoundError :
	      	print("File Not Found!")
	      	
#------------------------------------
	      	
def find_student(search_name) :
	i = 1
	try :
				file = open("students.txt", "r")
				content = file.readlines()
				
				for line in content :
					
					if search_name in line :
						print(f"{i}. {line}", end="")
					else :
						print("Student not found!")
				
					i+=1
										
	except FileNotFoundError :
	      	print("File Not Found!")

	      		      	
#------------------------------------
	      	
def main() :
	
	choice = 0
	
	while choice != 4 :
		print("\n================================")
		print("\t\tStudent Record Management")
		print("================================")
		
		print("\n1. Save Student Records")
		print("2. Read Student Records")
		print("3. Search Student")
		print("4. Exit From Program")
				
		try :
			choice = int(input("\nEnter Your Choice(1, 2, 3, 4) : "))
			
		except ValueError :
			print("\nError : Please enter digits")
		
		# ----------
		
		if choice == 1 :
			
			n = int(input("\nHow many student records you want to enter?: "))
			for i in range(0, n) :
				print(f"\nEnter Student {i+1} Deatils: ")
				
				try :
					name = input("Enter Name: ")
					age = int(input("Enter Age: "))
					city = input("Enter City: ")
				
				except UnboundLocalError:
					print("\nPlease Enter Valid Information")
				except ValueError :
					print("\nPlease Enter Digits here")
					
			save_students(name, age, city)
			
			print("\nStudent Records saved Successfully. ✓")
		
		#----------
	
		elif choice == 2 :
			print("\nStudents Details: ")
			read_students()
		
		#----------
		
		elif choice == 3 :
			name = input(("\nEnter Student Name: "))
			find_student(name)
			
		
		#----------
		
		elif choice == 4 :
			print("\nThank You....")
			
		#----------
		
		else :
			print("\nInvalid Choice!")


#------------------------------------

main()