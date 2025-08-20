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


# Admin creates restaurant
restaurant = Restaurant("Food Haven")

# Admin adds employees
admin.add_Employees(restaurant, Employee("Rahim", "01711111111", "rahim@gmail.com", "Dhaka", 30, "Manager", 50000))
admin.add_Employees(restaurant, Employee("Karim", "01822222222", "karim@gmail.com", "Chittagong", 25, "Developer", 40000))

admin.view_Employees(restaurant)

# Admin adds menu items
admin.add_new_items(restaurant, Food_Items("Pizza", 1200, 4))
admin.add_new_items(restaurant, Food_Items("Burger", 500, 10))
admin.add_new_items(restaurant, Food_Items("Pasta", 800, 6))

# Create a customer
customer = Customer("Sifat", "01999999999", "sifat@gmail.com", "Sylhet")

# Customer views the menu
customer.view_menu_items(restaurant)

# Customer adds to cart
customer.add_to_cart(restaurant, "Pizza", 2)
customer.add_to_cart(restaurant, "Burger", 12)

# Customer views cart
customer.view_cart_items()



        