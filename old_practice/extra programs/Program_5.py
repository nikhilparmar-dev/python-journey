# Write a Python program to convert kilometers to miles.
# Date : 29/01/2026
# Author : Nikhil

kilometers = float(input("Enter kilometers: "))

# Conversion factor: 1 kilometer = 0.621371 miles
conversion_factor = 0.621371

miles = kilometers * conversion_factor

print(f"{kilometers} is miles = {miles}")