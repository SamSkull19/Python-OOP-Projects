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
            
def admin_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter Your Address : ")
    admin = Admin(name=name, email=email, phone=phone, address=address)
    
    while True:
        print(f'Welcome {admin.name}!!')
        print(f'1. Add New Food Items')
        print(f'2. Add New Employee')
        print(f'3. View Employees')
        print(f'4. View Food Items')
        print(f'5. Delete Food Items')
        print(f'6. Exit')

        choice = int(input('Enter your Choice : '))

        if choice == 1:
            item_name = input("Enter Item Name : ")
            item_price = int(input("Enter Item Price : "))
            item_quantity = int(input("Enter Item Quantity : "))

            item = Food_Items(item_name, item_price, item_quantity)
            admin.add_new_items(neffroxx, item)

        elif choice == 2:
            name = input("Enter employee name : ")
            phone = input("Enter employee phone : ")
            email = input("Enter employee email : ")
            address = input("Enter employee address : ")
            age = input("Enter employee age : ")
            designation = input("Enter employee designation : ")
            salary = input("Enter employee salary : ")

            employee = Employee(name, phone, email, address, age, designation, salary)
            admin.add_Employees(neffroxx, employee)

        elif choice == 3:
            admin.view_Employees()

        elif choice == 4:
            admin.view_menu()
            
        elif choice == 5:
            item_name = input("Enter Item Name : ")
            admin.remove_item(neffroxx, item_name)
            
        elif choice == 6:
            break;
        
        else:
            print('Invalid Choice')