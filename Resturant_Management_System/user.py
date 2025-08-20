# USER
# Admin
# Employee
# Customer

from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

    def __repr__(self):
        return f'Name : {self.name} | Phone : {self.phone} | Email : {self.email} | Address : {self.address} | Age : {self.age} | Designation : {self.designation} | Salary : {self.salary}'

class Admin(User):
    def __init__(self, name, phone, email, address, age):
        super().__init__(name, phone, email, address)
        self.age = age
        
    def add_Employees(self, restaurant, employee):
        restaurant.add_Employees(employee)

    def view_Employees(self, restaurant):
        restaurant.view_Employees()
        
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = [] # This is our employee database

    def add_Employees(self, employee):
        self.employees.append(employee)

    def view_Employees(self):
        print('Employee List : ')
        for emp in self.employees:
            print(emp)

admin = Admin('Samin', '12352552', 'sifatsamin@gmail.com', 'Cumilla', 24)
print(admin.name)
print(admin.email)
print(admin.age)

# Create restaurant
restaurant = Restaurant("Food Haven")

admin.add_Employees(restaurant, Employee("Rahim", "01711111111", "rahim@gmail.com", "Dhaka", 30, "Manager", 50000))
admin.add_Employees(restaurant, Employee("Karim", "01822222222", "karim@gmail.com", "Chittagong", 25, "Developer", 40000))

admin.view_Employees(restaurant)

        