# File Handling

# 1. Writing To a File :
file = open("notes.txt", "w")
file.write("Hello i'm Nikhil")
file.write("\nI'm 17 years old")
print("File writing done")
file.close()


# 2. Reading from a File :
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()


# 3. readline() - reads only one line :
file = open("notes.txt", "r")
content = file.readline()
print(content) 
file.close()


# 4. readlines() - reads all lines as list : 
file = open("notes.txt", "r")
content = file.readlines()
print(content) 
file.close()


# 5. Append to a File :
file = open("notes.txt","a")
file.write("\nI'm From kadi")
print("Append done : ")

file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()



# 6. with Statement - no need to close
with open("notes.txt", "r") as f :
	print(f.read())
	

# 7. file handling with exceptions :
try :
	file = open("notes.txt", "r")
	print("File Found")
	print(file.read())
	
except FileNotFoundError :
	print("File Not Found")

except PermissionError :
	print("Not permission to open file")
	
	
	
# 8. Check if file exists :
import os

if os.path.exists("notes.txt") :
	print("\nFile Found")
	
else :
	print("\nFile Not Found")