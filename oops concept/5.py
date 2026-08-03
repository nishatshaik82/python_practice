#create an employee class and drive manager and developer
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

class Manager(Employee):
    def display_info(self):
        print("Manager Name:", self.name)
        print("Salary:", self.salary)

class Developer(Employee):
    def display_info(self):
        print("Developer Name:", self.name)
        print("Salary:", self.salary)

manager = Manager("Ramesh", 70000)
developer = Developer("Priya", 50000)

manager.display_info()
developer.display_info()