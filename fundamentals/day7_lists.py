
skills = ["Python", "Django", "MySQL"]

# ADD
skills.append("FastAPI")
skills.insert(1, "Java")
skills.extend(["SQLite"])
print(skills)


# REMOVE
skills.remove("Java")
skills.pop()
skills.pop(2)
del skills[1]
print(skills)


#SEARCH
print(skills.index("Python"))
print("Java" in skills)


# INFO
print(len(skills))
print(skills.count("Python"))


# ORDER
skills.sort()
skills.sort(reverse=True)
skills.reverse()
print(skills)


# COPY
new = skills.copy()
new_2 = skills[:]
print(new)
print(new_2)


# CLEAR
skills.clear()


# LIST SLICING
nums = [0,1,2,4,5,6,7,8,9]

print(nums[2:5])
print(nums[0:4])
print(nums[6:])
print(nums[::2])
print(nums[::-1])
print(nums[1:8:2])


# LIST COMPREHENTION
squares = []

#1. NORMAL WAY -
for i in range(1,6) :
	squares.append(i * i)
print(squares)


#2. Comprehantion -
squares = [x*x for x in range(1, 6)]
print(squares)


#3. with Condition -
squares = [x * x for x in range(1,6 ) if x %2 == 0]
print(squares)


#4. Transform strings :
skills = ["python", "django", "sql"]
skills = [s.upper() for s in skills]
print(skills)
