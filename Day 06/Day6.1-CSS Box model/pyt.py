class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
         
    def showDetails(self):
        print("role = ", self.role)
        print("dept = ", self.dept)
        print("salary = ", self.salary)
        
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("engineer", "IT", "80,000")
        
    def showDetails(self):
        print("name = ", self.name)
        print("age = ", self.age)
        print("role = ", self.role)
        print("dept = ", self.dept)
        print("salary = ", self.salary)
        
        
e1 = Engineer("Dave", 56)
e1.showDetails()

e2 = Employee("DEE", "er", "sdsd")
e2.showDetails()