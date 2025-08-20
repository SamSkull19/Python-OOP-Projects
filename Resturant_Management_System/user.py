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
        return f'Name : {self.name} |\t Phone : {self.phone} |\t Email : {self.email} |\t Address : {self.address} |\t Age : {self.age} |\t Designation : {self.designation} |\t Salary : {self.salary}'

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

class Menu:
    def __init__(self):
        self.items = [] # Database of menu items
    
    def add_menu_items(self, item):
        self.items.append(item)
    
    def find_items(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
            return None    

    def remove_item(self, item_name):
        item = self.find_items(item_name)
        
        if item:
            self.items.remove(item)
            print("Items Deleted")

        else:
            print("Item not Found")

    def show_menu_items(self):
        print('**** MENU ****')
        print('Name\tPrice\tQuantity')
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')

class Food_Items:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity



admin = Admin('Samin', '12352552', 'sifatsamin@gmail.com', 'Cumilla', 24)
print(admin.name)
print(admin.email)
print(admin.age)

# Create restaurant
restaurant = Restaurant("Food Haven")

admin.add_Employees(restaurant, Employee("Rahim", "01711111111", "rahim@gmail.com", "Dhaka", 30, "Manager", 50000))
admin.add_Employees(restaurant, Employee("Karim", "01822222222", "karim@gmail.com", "Chittagong", 25, "Developer", 40000))

admin.view_Employees(restaurant)

menu = Menu()
item = Food_Items('Pizza', 1200, 4)

menu.add_menu_items(item)
menu.show_menu_items()


        