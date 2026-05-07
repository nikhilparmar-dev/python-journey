print("Coditions :\n")

print("1. Basic if/elif/else: ")
age = 20
if age >= 18 :
	print("Adult")
elif age >= 14 :
	print("Teen")
elif age >= 9 :
	print("Kid")
else :
	print("Child")

		
has_degree = False
if age >= 18 and has_degree :
	print("Eligible")
elif age < 18 and has_degree :
	print("Not eligible")
else :
	print("Get degree First")
	
	

print("\n2. Nested if: ")
salary = 50000
experience = 2
if salary >= 50000 :
	if experience >= 1:
		print("Senior Level")
	else :
		print("Fresher level")
else :
	print("Low salary Band")
	
status = "Adult" if age >= 18 else "Minor"
print(status)



print("\n\nLoops :\n")

print("1. For Loop: ")
for i in range(1, 6) :
	print(i, end=", ")

fruits = ["\nBanana", "Mango", "Orange"]
for fruit in fruits :
	print(fruit)
	
Name = "Nikhil"
for letter in Name :
	print(letter, end=", ")
print()

for j in range(1, 6) :
	if j == 3 :
		continue
	print(j, end=", ")
print()

for n in range(1, 6) :
	if n == 3 :
		break
	print(n, end=", ")
	
	
	
print("\n\n2. While Loop: ")
i = 1
while i <= 5 :
	print(i, end="")
	i += 1
print()
	
password = ""
while password != 123 :
	password = int(input("Enter Password: "))
print("Login Success")



print("\n\n3. Nested Loop: ")
i = 1
j = 1

while i <= 5 :
	while j <= 5 :
		print(i, j)
		j += 1
	print()
	i += 1
	
for i in range(1, 6) :
	for j in range (0, i) :
		print(i, end="")
	print()