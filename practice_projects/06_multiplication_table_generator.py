# Mini Project #6 -  Multiplication Tables Generator (Loops)
# Date: 16/02/2026
# Author: Nikhil


start = int(input("Enter statrting Number: "))
end = int(input("Enter Ending Number: "))

for i in range(start, end + 1) :

    print("----------------------")

    print(f"\nTable of {i}: ")

    for j in range(1, 11) :

        print(f"{i} x {j} = {i*j}")