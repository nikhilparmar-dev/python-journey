# Program 6 — OOP — Employee Class

""" Create class Employee:
- __init__(name, salary, department)
- __salary is private
- get_salary() → returns salary
- give_raise(amount) → adds to salary
- __str__() → "Nikhil | IT Dept | Rs.35000"

Create child class Manager(Employee):
- Add team_size attribute
- Override __str__() to include team_size 

Create 2 objects — test all methods """

class Employee :
	def __init__(self,name, salary, department) :
		self.name = name
		self.__salary = salary
		self.department = department
		
	def get_salary(self) :
		return self.__salary
		
	def give_raise(self, amount) :
		self.__salary += amount
		print("RAISED DONE")
		
	def __str__(self) :
		return f"{self.name} | {self.department} | Rs.{self.__salary}"
		
		
		
class Manager(Employee) :
	def __init__(self, name, salary, department, team_size) :
		super().__init__(name, salary, department)
		self.team_size = team_size
		
	def __str__(self) :
		return f"{self.name} | {self.department} | Rs. {self.get_salary()} | Team Size : {self.team_size}"
		
		
e = Employee("Nikhil", 35000, "IT Dept")
print(e.get_salary())
e.give_raise(5000)
print(e.__str__())

m = Manager("Prem", 41000, "HR Dept", 12)
print(m.get_salary())
m.give_raise(-2000)
print(m.__str__())