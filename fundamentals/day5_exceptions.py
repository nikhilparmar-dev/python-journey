
# Exceptions

# 1. Basic try/except :
try :
	age = int(input("Enter An Number: "))
except ValueError :
	print("Please Enter an Number")
	
	
# 2. All causes try/except/else/finally :
try :
	number = int(input("Enter an Number: "))
	result = 100/number
	
except ValueError :
	print("Please enter an number")
	
except ZeroDivisionError :
	print("Cannot divided by zero")

else :
	print(f"Result: {result}")

finally :
	print("Always Runs.")
	
	
# 3. Multiple Exceptions :
try :
	no = int(input("Enter an Number: "))
	
except (ValueError, ZeroDivisionError) :
	print("Enter An non zero number: ")
	

# 4. Custom Error :
def set_age(age) :
	if age <= 0 :
		raise ValueError("Invalid Age here")
	return age
		
try :
	set_age(-5)
except ValueError as e :
	print(e)
	
	

# 5. Custom Class Error :
class InvalidAgeError(Exception) :
	pass

def set_age(age) :
	if age < 0 :
		raise InvalidAgeError("Please enter valid age")

try :
	set_age(-3)
except InvalidAgeError as e :
	print("Error : ", e)