from food_items import Food_Items
from menu import Menu
from order import Order
from restaurant import Restaurant
from user import Customer, Employee, Admin

neffroxx = Restaurant("Neffroxx")

def customer_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter Your Address : ")
    customer = Customer(name=name, email=email, phone=phone, address=address)
    
    while True:
        print(f'Welcome {customer.name}!!')
        print(f'1. View Menu')
        print(f'2. Add items to Cart')
        print(f'3. View Cart')
        print(f'4. Pay Bill')
        print(f'5. Exit')

