class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        super().display()
        print("Dept:",self.department)
e1=Employee("Lucky",100000)
m1=Manager("Mary",19289,"HR")
e1.display()
m1.display()
