# Program 1 — Profile Card

# Create variables for:
# name, age, city, course, is_employed, skills (list)
# Print a formatted profile card using all variables
# Use f-string formatting 

name = input("Enter Your name: ")
age = int(input("Enter Your Age: "))
city = input("Enter Your city: ")
course = input("Enter Your course: ")
emp = input("Are you employeed? (y/n) : ")

if emp == "y" :
	Employeed = True
else :
	Employeed = False
	
n = int(input("How Many skills you have?: "))

skills = []
for i in range(n) :
	skill = input(f"Enter Your skill {i+1} : ")
	skills.append(skill)
	
profile = {
"name" : name,
"age" : age,
"city" : city,
"course" : course,
"is_employed" : Employeed,
"skills" : skills
}

print()
for key, value in profile.items() :
	print(f"{key} : {value}")
