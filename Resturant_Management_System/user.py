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

emp = Employee('Samin', '12352552', 'sifatsamin@gmail.com', 'Cumilla', 24, 'Waiter', 10000)
print(emp.name)
print(emp.email)
print(emp.age)
print(emp.salary)
        