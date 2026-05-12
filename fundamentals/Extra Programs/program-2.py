# Program 2 — Grade Calculator

""" Take 5 subject marks as input from user
# Calculate average
# Print grade:
#  90+  → A+
  80+  → A
  70+  → B
  60+  → C
  below 60 → Fail """
  
name = input("Enter Your Name: ")
 
Gujarati = int(input("Enter Your Gujarati Marks: "))
Maths = int(input("Enter Your Maths Marks: "))
Science = int(input("Enter Your Science Marks: "))
Psychology = int(input("Enter Your Psychology Marks: "))
English = int(input("Enter Your English Marks: "))
 
avg = (Gujarati + Maths + Science +  Psychology + English) / 5

if 90 <= avg <= 100 :
	print("GRADE : A+")

elif 80 <= avg <= 89 :
	print("GRADE : A")
	
elif 70 <= avg <= 79 :
	print("GRADE : B")
	
elif 60 <= avg <= 69 :
	print("GRADE : C")

elif avg <= 59 :
	print("FAIL")

else :
	print("Invalid Marks Entered")