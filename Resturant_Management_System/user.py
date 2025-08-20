# USER
# Admin
# Employee
# Customer

from abc import ABC
from order import Order

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
    
class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()
    
    def view_menu_items(self, restaurant):
        restaurant.menu.show_menu_items()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_items(item_name)

        if item:
            if quantity > item.quantity:
                print("Item quantity Exceeded")
            else:
                item.quantity = quantity
                self.cart.add_items(item)
        else:
            print(f'Item : {item_name} not found')

    def view_cart_items(self):
        print('*** Cart ***')
        print('Name\tPrice\tQuantity')

        for item, quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        
        print(f'Total Price : {self.cart.total_price}')



class Admin(User):
    def __init__(self, name, phone, email, address, age):
        super().__init__(name, phone, email, address)
        self.age = age
        
    def add_Employees(self, restaurant, employee):
        restaurant.add_Employees(employee)

    def view_Employees(self, restaurant):
        restaurant.view_Employees()

    def add_new_items(self, restaurant, item):
        restaurant.menu.add_menu_items(item)
    
    def remove_item(self, restaurant, item):
        restaurant.menu.remove_item(item)
        




        