# app.py
import streamlit as st
from food_items import Food_Items
from restaurant import Restaurant
from user import Customer, Employee, Admin
import pandas as pd

# Initialize Restaurant in session state
if "restaurant" not in st.session_state:
    st.session_state.restaurant = Restaurant("Neffroxx")

neffroxx = st.session_state.restaurant

# Streamlit UI
st.set_page_config(page_title="Restaurant Management", page_icon="🍴")
st.title(f"🍴👋 Welcome to {neffroxx.name} Restaurant")

st.markdown("Please select your role to continue:")

with st.expander("Login as"):
 	role = st.selectbox(
        "Choose your role:",
        ["Role", "Customer", "Admin"]
    )

# CUSTOMER UI
if role == "Customer":
    st.header("🧑‍🍳 Customer Panel")

    if "customer" not in st.session_state:
        with st.form("customer_form"):
            st.subheader("Enter Your Details")
            name = st.text_input("Name")
            phone = st.text_input("Phone")
            email = st.text_input("Email")
            address = st.text_input("Address")
            submitted = st.form_submit_button("Start")
            if submitted and name:
                st.session_state.customer = Customer(name, phone, email, address)
                st.success(f"Welcome {name}!")


    if "customer" in st.session_state:
        customer = st.session_state.customer

        menu_choice = st.selectbox("Choose Action", [
            "View Menu", "Add to Cart", "View Cart", "Pay Bill"
        ])

        if menu_choice == "View Menu":
            st.subheader("📜 Menu Items")
            if neffroxx.menu.items:
                # Create lists for table
                item_names = [item.name for item in neffroxx.menu.items]
                prices = [item.price for item in neffroxx.menu.items]
                quantities = [item.quantity for item in neffroxx.menu.items]

                # Create DataFrame
                df = pd.DataFrame({
                    "Item Name": item_names,
                    "Price ($)": prices,
                    "Quantity": quantities
                })

                # Display as a table
                st.table(df)
            else:
                st.warning("No items available yet!")

        elif menu_choice == "Add to Cart":
            st.subheader("🛒 Add Item to Cart")
            if neffroxx.menu.items:
                # Select item
                item_name = st.selectbox("Select Item", [item.name for item in neffroxx.menu.items])
                quantity = st.number_input("Quantity", min_value=1, step=1)

                # Find the selected item object
                selected_item = next((item for item in neffroxx.menu.items if item.name == item_name), None)

                if st.button("Add to Cart") and selected_item:
                    if quantity > selected_item.quantity:
                        st.warning(f"❌ Not enough quantity available. Only {selected_item.quantity} left.")
                        
                    else:
                        customer.add_to_cart(neffroxx, item_name, quantity)
                        st.success(f"{quantity} x {item_name} added to cart")

            else:
                st.warning("No items available to order!")


        elif menu_choice == "View Cart":
            st.subheader("🛍️ Cart Items")
            if customer.cart.items:
                # Prepare data for table
                item_names = [item.name for item, qty in customer.cart.items.items()]
                prices = [item.price for item, qty in customer.cart.items.items()]
                quantities = [qty for item, qty in customer.cart.items.items()]
                totals = [item.price * qty for item, qty in customer.cart.items.items()]

                # Create DataFrame
                df = pd.DataFrame({
                    "Item Name": item_names,
                    "Price ($)": prices,
                    "Quantity": quantities,
                    "Total ($)": totals
                })

                # Display table
                st.table(df)  # or st.dataframe(df) for scrollable table
                st.write(f"**Total Price: ${customer.cart.total_price}**")
            else:
                st.info("Cart is empty")

        elif menu_choice == "Pay Bill":
            if customer.cart.items:
                st.success(f"✅ Paid ${customer.cart.total_price} successfully")
                customer.pay_bill()
            else:
                st.warning("Cart is empty")



# ADMIN UI
elif role == "Admin":
    st.header("👨‍💼 Admin Panel")

    if "admin" not in st.session_state:
        with st.form("admin_form"):
            st.subheader("Enter Admin Details")
            name = st.text_input("Name")
            phone = st.text_input("Phone")
            email = st.text_input("Email")
            address = st.text_input("Address")
            submitted = st.form_submit_button("Login")
            if submitted and name:
                st.session_state.admin = Admin(name, phone, email, address)
                st.success(f"Welcome Admin {name}!")

    if "admin" in st.session_state:
        admin = st.session_state.admin

        menu_choice = st.selectbox("Choose Action", [
            "Add Food Item", "View Food Items", "Delete Food Item",
            "Add Employee", "View Employees"
        ]
        )

        if menu_choice == "Add Food Item":
            with st.form("food_form"):
                st.subheader("➕ Add New Food Item")
                item_name = st.text_input("Item Name")
                item_price = st.number_input("Price", min_value=1)
                item_quantity = st.number_input("Quantity", min_value=1)
                submitted = st.form_submit_button("Add")
                if submitted and item_name:
                    item = Food_Items(item_name, item_price, item_quantity)
                    admin.add_new_items(neffroxx, item)
                    st.success(f"Added {item_name} successfully")

        elif menu_choice == "View Food Items":
            st.subheader("📜 Food Menu")
            if neffroxx.menu.items:
                # Create lists for table
                item_names = [item.name for item in neffroxx.menu.items]
                prices = [item.price for item in neffroxx.menu.items]
                quantities = [item.quantity for item in neffroxx.menu.items]

                # Create DataFrame
                df = pd.DataFrame({
                    "Item Name": item_names,
                    "Price ($)": prices,
                    "Quantity": quantities
                })

                # Display as a table
                st.table(df)

            else:
                st.warning("No food items available")

        elif menu_choice == "Delete Food Item":
            if neffroxx.menu.items:
                item_name = st.selectbox("Select Item", [item.name for item in neffroxx.menu.items])
                if st.button("Delete"):
                    admin.remove_item(neffroxx, item_name)
                    st.success(f"Deleted {item_name}")
            else:
                st.warning("No items to delete")

        elif menu_choice == "Add Employee":
            with st.form("emp_form"):
                st.subheader("➕ Add Employee")
                name = st.text_input("Employee Name")
                phone = st.text_input("Phone")
                email = st.text_input("Email")
                address = st.text_input("Address")
                age = st.number_input("Age", min_value=18, max_value=70)
                designation = st.text_input("Designation")
                salary = st.number_input("Salary", min_value=0)
                submitted = st.form_submit_button("Add")
                if submitted and name:
                    employee = Employee(name, phone, email, address, age, designation, salary)
                    admin.add_Employees(neffroxx, employee)
                    st.success(f"Added employee {name}")

        elif menu_choice == "View Employees":
            st.subheader("👥 Employee List")
            if neffroxx.employees:
                import pandas as pd
        
                # Create lists for each attribute
                names = [emp.name for emp in neffroxx.employees]
                phones = [emp.phone for emp in neffroxx.employees]
                emails = [emp.email for emp in neffroxx.employees]
                addresses = [emp.address for emp in neffroxx.employees]
                ages = [emp.age for emp in neffroxx.employees]
                designations = [emp.designation for emp in neffroxx.employees]
                salaries = [emp.salary for emp in neffroxx.employees]
        
                # Create DataFrame
                df = pd.DataFrame({
                    "Name": names,
                    "Phone": phones,
                    "Email": emails,
                    "Address": addresses,
                    "Age": ages,
                    "Designation": designations,
                    "Salary ($)": salaries
                })
        
                # Display table
                st.table(df)  # or st.dataframe(df) for scrollable table
            else:
                st.warning("No employees added yet")

