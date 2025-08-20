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

        choice = int(input('Enter your Choice : '))

        if choice == 1:
            customer.view_menu_items(neffroxx)

        elif choice == 2:
            item_name = input('Enter item name : ')
            quantity = int(input('Enter item quantity : '))
            customer.add_to_cart(neffroxx, item_name, quantity)
        
        elif choice == 3:
            customer.view_cart_items()

        elif choice == 4:
            customer.pay_bill()
            
        elif choice == 5:
            break
            
        else:
            print('Invalid Choice')