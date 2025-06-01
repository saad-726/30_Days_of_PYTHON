#name,id ,salary functions raise annual salary details
class Employee:
    def __init__ (self,name,Id,salary):
        self.name=name
        self.salary=salary
        self.id=Id
    def annual_salary(self):
        print(f"The annual salary of employee {self.name} is : {self.salary *12}")
    def display(self):
        print("----Details of Employee----")
        print("Name :",self.name)
        print("Id :",self.id)
        print(f"Salary :{self.salary}/month")
    def incremented(self,percentage):
        print(f"After applying raise salary is {(self.salary*(percentage/100)+self.salary)}/month")
e=Employee("Saad",123,17000)
e.annual_salary()
e.display()
e.incremented(10)