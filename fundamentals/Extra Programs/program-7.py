# Program 7 — Exception Handling

""" Write a function safe_divide(a, b):
- If b is 0 → raise ZeroDivisionError
- If a or b is not a number → raise TypeError
- Otherwise → return result

Wrap in try/except/else/finally
Test with 3 different inputs:
- Normal numbers
- Zero as divisor
- String as input """


def safe_divide(a, b):
	if b == 0 :
		raise ZeroDivisionError("Cannot Devided by zero")
		
	if type(a) not in [int, float] or type(b) not in [int, float]:
		raise TypeError("Please enter an number here")
		
	result = a/b 
	return result
	
try :
	print(safe_divide(a=10, b=5))
	print(safe_divide(10, 0))
	print(safe_divide(10,"5"))
	
except ZeroDivisionError as z:
		print(z)
		
except TypeError as t:
	print(t)

finally :
	print("done")
