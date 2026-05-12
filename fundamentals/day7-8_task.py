# Student Grade Manager:
	
students = [
    {"name": "Nikhil", "marks": [85, 90, 78, 92, 88]},
    {"name": "Rahul",  "marks": [70, 65, 80, 75, 72]},
    {"name": "Priya",  "marks": [95, 98, 92, 96, 99]},
    {"name": "Amit",   "marks": [50, 55, 48, 60, 52]},
]



# 1. Use list comprehension to create a new list of student names only

names = []

for item in students :
	names.append(item["name"])
	
print(names)



# 2. Use dict comprehension to create:

i = 0
average_marks = {}

for item in students :
	average_marks.update({item["name"] : sum(item.get("marks")) / len(item.get("marks"))})

print(f"\n{average_marks}")



# 3. Find and print:
#    → Highest average scorer
max = 0
for key, score in average_marks.items() :
	if score > max : 
		max = score
		name = key

print(f"\nHighest Scorer = {name} : {max}")
	

#    → Lowest average scorer
low = 0
for key, score in average_marks.items() :
	if score < max : 
		max = score
		name = key

print(f"Lowest Scorer = {name} : {max}")



# 4. Use a set to find:
#   → All unique marks across all students

mark = 0
unique_marks = set({})
	
for item in students :
	mark = (item.get("marks"))
	
	for m in mark :
		unique_marks.add(m)
	
print(f"\nUnique Marks : {unique_marks}")

#   → How many unique marks exist
print(f"Total Unique Marks : {len(unique_marks)}")



# 5. Sort students by average — highest to lowest

sorted_dict = dict(
    sorted(average_marks.items(), key=lambda item: item[1], reverse=True)
)

print("\n", sorted_dict)
	