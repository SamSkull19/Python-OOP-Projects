from menu import Menu
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = [] # This is our employee database
        self.menu = Menu()

    def add_Employees(self, employee):
        self.employees.append(employee)

    def view_Employees(self):
        print('Employee List : ')
        for emp in self.employees:
            print(emp)