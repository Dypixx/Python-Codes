# pip install pandas
# pip install openpyxl

import os
from datetime import datetime
import pytz
import pandas as pd

IST = pytz.timezone('Asia/Kolkata')
orders = {}
folder_path = os.path.expanduser("~/Documents/Shop Orders")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, "Shop_Orders.xlsx")


# Load existing orders from Excel (if available)
if os.path.exists(file_path):
    df = pd.read_excel(file_path, index_col="Order ID")
    orders = df.to_dict(orient="index")

# Function to generate a unique 4-digit order ID
def generate_order_id():
    return f"{len(orders) + 1:04d}"

# Save all orders to Excel automatically
def save_to_excel():
    df = pd.DataFrame.from_dict(orders, orient="index")
    df.to_excel(file_path, index_label="Order ID")
    print(f"Orders updated successfully in {file_path}!")

# Add a new order
def add_order():
    name = input("Enter customer name: ").strip()
    item = input("Enter ordered item: ").strip()
    order_id = generate_order_id()
    order_time = datetime.now(IST).strftime("%d-%m-%Y %I:%M:%S %p")
    orders[order_id] = {
        "Customer Name": name,
        "Order Items": [item],
        "Order Time": order_time,
    }
    print(f"Order added successfully! Order ID: {order_id}")
    save_to_excel()

# Add new items to an existing order
def add_new_items():
    order_id = input("Enter Order ID to add items: ").strip()
    if order_id in orders:
        new_item = input("Enter new item to add to the order: ").strip()
        orders[order_id]["Order Items"].append(new_item)
        print("New item added successfully!")
        save_to_excel()
    else:
        print("Order not found.")

# Change the details of an existing order
def change_order():
    order_id = input("Enter Order ID to change: ").strip()
    if order_id in orders:
        print("\nCurrent Order Details:")
        for key, value in orders[order_id].items():
            print(f"{key}: {value}")
        print("\nEnter new details:")
        name = input("Enter new customer name: ").strip()
        item = input("Enter new ordered item: ").strip()
        order_time = datetime.now(IST).strftime("%d-%m-%Y %I:%M:%S %p")
        orders[order_id] = {
            "Customer Name": name,
            "Order Items": [item],
            "Order Time": order_time,
        }
        print("Order updated successfully!")
        save_to_excel()
    else:
        print("Order not found.")

# Search for an order
def search_order():
    order_id = input("Enter Order ID to search: ").strip()
    order = orders.get(order_id)
    if order:
        print("\nOrder Details:")
        for key, value in order.items():
            print(f"{key}: {value}")
    else:
        print("Order not found.")

# Display all orders
def display_all_orders():
    if orders:
        print("\nAll Orders:")
        for order_id, details in orders.items():
            print(f"\nOrder ID: {order_id}")
            for key, value in details.items():
                print(f"  {key}: {value}")
    else:
        print("No orders available.")

# Admin pannel
def menu():
    while True:
        print("\n--- Shop Management ---")
        print("1. Add New Order")
        print("2. Add New Items to Existing Order")
        print("3. Change Order Details")
        print("4. Search Order by Order ID")
        print("5. Display All Orders")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_order()
        elif choice == "2":
            add_new_items()
        elif choice == "3":
            change_order()
        elif choice == "4":
            search_order()
        elif choice == "5":
            display_all_orders()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Created By @Dypixx
menu()
