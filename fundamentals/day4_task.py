
# Bank System Using OOP

class BankAccount :

    def __init__(self, owner, balance) :
        self.owner = owner
        self.__balance = balance # Private


    def deposit(self, amount) :
        self.__balance += amount


    def withdraw(self, amount) :

        if amount <= self.__balance :
            self.__balance -= amount
            print("Deduction Done")
        else :
            print("Insufficient balance")


    def get_balance(self) :
        return self.__balance


    def __str__(self) :
        return f"Account: {self.owner} | Balance: {self.__balance}"



class SavingAccount(BankAccount) :
    interest_rate = 0.5

    def add_Interest(self) :
        balance = self.get_balance()
        self.deposit(balance * self.interest_rate)



obj1 = BankAccount("Nikhil", 5000)
obj2 = SavingAccount("Prem", 3000)

obj2.deposit(3000)
print(obj2.get_balance())
obj2.add_Interest()
print(obj2.get_balance())