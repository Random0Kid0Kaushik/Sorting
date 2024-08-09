from collections import deque

# Create a dictionary of stationary objects
stationary_dict = {}
restocking_queue = deque()

class RestockDetail:
    def __init__(self, prod_id, quantity):
        self.prod_id = prod_id
        self.quantity = quantity

    def get_prod_id(self):
        return self.prod_id

    def get_quantity(self):
        return self.quantity

# Existing functions ...

def restock_stationary(stationary_dict):
    prod_id = input("Enter product id: ")
    if prod_id not in stationary_dict:
        print("Invalid product id! Please try again!")
        return
    quantity = int(input("Enter qty to restock: "))
    restock_detail = RestockDetail(prod_id, quantity)
    restocking_queue.append(restock_detail)
    print("Restocking arrival queued successfully!\n")

def view_restock_queue():
    print(f"Number of restocking deliveries in queue: {len(restocking_queue)}")

def handle_next_delivery(stationary_dict):
    if not restocking_queue:
        print("No deliveries in the queue!\n")
        return

    next_delivery = restocking_queue.popleft()
    prod_id = next_delivery.get_prod_id()
    quantity = next_delivery.get_quantity()
    stationary = stationary_dict[prod_id]

    print("Display Pending stock arrival:")
    print("-" * 30)
    print(f"Product ID: {prod_id}")
    print(f"Product Name: {stationary.get_prod_name()}")
    print(f"Product Category: {stationary.get_category()}")
    print(f"Brand: {stationary.get_brand()}")
    print(f"Supplier Year: {stationary.get_supplier()}")
    print(f"Stock remaining: {stationary.get_stock()}")
    print("-" * 30)
    print(f"New Stock: {quantity}")
    print("=" * 30)

    proceed = input("Proceed with restocking (Y/N): ").strip().upper()
    if proceed == 'Y':
        stationary.set_stock(stationary.get_stock() + quantity)
        print(f"Updated stock for {prod_id}: {stationary.get_stock()}")
        print(f"{len(restocking_queue)} deliveries remaining in the queue.")
    else:
        restocking_queue.append(next_delivery)
        print(f"Product {prod_id} re-queued!")

def restocking_menu(stationary_dict):
    while True:
        print("Restocking Menu:")
        print("1. Enter new stock arrival")
        print("2. View number of stock arrivals")
        print("3. Handle next restock in queue")
        print("0. Return to Main Menu.")
        choice = input("Please select one: ")

        if choice == "1":
            restock_stationary(stationary_dict)
        elif choice == "2":
            view_restock_queue()
        elif choice == "3":
            handle_next_delivery(stationary_dict)
        elif choice == "0":
            break
        else:
            print("Invalid choice! Please try again.\n")

# Existing main_menu and populate_data functions ...
