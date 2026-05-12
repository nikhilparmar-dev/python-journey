# Program 4 — List Operations


# Create a list of 5 city names
city = ["Kadi", "Kalol", "Ahmedabad", "Gandhinagar", "Delhi"]


# - Sort alphabetically and print
city.sort()
print(city)


# - Add 2 more cities
city.extend(["Mumbai", "Kolkata"])
print(city)


# - Remove one city by name
city.remove("Kolkata")
print(city)


# - Print total count
print(f"Total Citys = {len(city)}")


# - Check if "Kadi" is in list
if "Kadi" in city :
	print("Yes, Kadi in List")
else :
	print("No kadi")
	
	
# - Print using list comprehension in UPPERCASE 
upper = [c.upper() for c in city]
print(upper)