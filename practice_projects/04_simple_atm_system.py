# Mini Project #4 -  Simple ATM System ( While Loop )
# Date: 12/02/2026
# Author: Nikhil


balance = 10000
choice = 0

while choice != 4 :

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1 :
        print("balance = ", balance)

    elif choice == 2 :
        amount = int(input("Enter Deposit Amount: "))
        balance += amount
        print("Deposited successfully!")

    elif choice == 3 :
        amount = int(input("Enter Amount to withdraw: "))

        if amount <= balance :
            balance -= amount 
            print("amount withdrawan!")
        else :
            print("Insufficient Balance !")

    elif choice ==  4 :
        print("Exited Successfully!")

print("Thank You!")