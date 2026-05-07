# ATM Machine Program:
	
balance = 10000
pin = 0
choice = 1

while pin != 1234 :
	pin = int(input("Enter Your Pin: "))
	
print("Login Success!")

while choice != 3 :
	print("\n\nATM MACHINE\n")
	print("1. Check Balance")
	print("2. Withdraw Money")
	print("3. Exit")
	
	choice = int(input("Enter Your Choice: "))
	
	if choice == 1 :
		print("\nYour Balance= ₹", balance)
		
	elif choice == 2 :
		amount = int(input("\nEnter Amount: "))
		if amount <= balance :
			balance -= amount
			print("Success!")
		else :
			print("Insufficient balance")

	else :
		print("Invalid choice!")
	
	
print("\nThank You")