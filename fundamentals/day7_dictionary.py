student = {
"name" : "nikhil",
"age" : 17,
"city" : "kadi",
"course" : "BCA"
}


# ACCESS 
print(student["name"])
print(student.get("name"))
print(student.get("name", "N/A"))


# UPDATE 
student["age"]  = 17
student["city"] = "Ahmedabad"
student.update({"city" : "Kadi", "course" : "MCA"})
print(student)


# REMOVE
student.pop("course")
del student["city"]
print(student)


# LOOP THROUGH
for key in student :
	print(key)
	
for value in student :
	print(value)
	
for key, value in student.items() :
	print(f"{key} : {value}")
	
	
# INFO
print(len(student))
print("name" in student)


# COPY
copy_stu = student.copy()
print(copy_stu)


# CLEAR
copy_stu.clear()
print(copy_stu)


# Nested Dictionary
Employees = {
"Total" : {
1 : {"Name" : "Nikhil", "Age" : 17}, 
2 : {"Name" : "Prem", "Age" : 18}
}
}
print(Employees["Total"])
print(Employees["Total"][1])
print(Employees["Total"][1]["Name"])


# LIST COMPREHNTION 
squares = {}
for i in range(1, 6) :
	squares[i] = i*i
print(squares)


squares = {i: i * i for i in range(1, 6)}
print(squares)