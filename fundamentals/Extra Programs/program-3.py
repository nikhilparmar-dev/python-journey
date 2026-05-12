# Program 3 — Multiplication Table

""" Ask user for a number
Print its multiplication table from 1 to 10
Using for loop
Format: "5 x 3 = 15" """

number = int(input("Enter an Number: "))

for i in range(1, 11) :
	print(f"{number} x {i} = {number*i}")