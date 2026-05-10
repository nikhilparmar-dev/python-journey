# Mini Project #5 - Bank Account System (Abtraction)
# Date: 09/03/2026
# Author: Nikhil


from abc import ABC, abstractmethod

class BankAccount :

    def __init__(self, name, balance) :
        self.name = name
        self.balance = balance

    @abstractmethod
    def deposit (self) :
        pass

    @abstractmethod
    def withdraw (self) :
        pass


class SavingAccount (BankAccount) :

    def deposit(self, amount) :
        self.balance += amount
        print("Deposit Success : ", amount, "Rs.")

    def withdraw(self, amount):
        if amount <= self.balance :
            print("Amount Withdrawn: ", amount)

        else :
            print("Insufficient Balance!")


class CurrenAccount (BankAccount) :

    def deposit(self, amount) :
        self.balance += amount
        print("Deposit Success : ", amount, "Rs.")

    def withdraw(self, amount):
        if amount <= self.balance :
            print("Amount Withdrawn: ", amount)

        else :
            print("Insufficient Balance!")


s = SavingAccount("Nikhil", 5000)
c = CurrenAccount("Prem", 7000)

print("\nSaving Account: ")
s.deposit(2000)
s.withdraw(3500)
print("Balance: ", s.balance)


print("\nCurrent Account: ")
c.deposit(2000)
c.withdraw(3500)
print("Balance: ", c.balance)