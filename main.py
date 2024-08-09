# Kaushik, 233050P, IT2153, Assignment 2

from sorting_algorithms import *
import datetime
from stationary import *
from restocking import *

# Create a dictionary of stationary objects
stationary_dict = {}

# Variables to store sorted lists
sorted_list = None


def add_stationary(stationary_dict):
    while True:
        prod_id = input("Enter Product ID: ")
        if prod_id in stationary_dict:
            print("Product ID already exists! \n")
            continue
        else:
            break
    prod_name = input("Enter Product Name: ")
    category = input("Enter Product Category: ")
    brand = input("Enter Brand: ")
    while True:
        supplier = input("Please enter the year this supplier started supplying this product: ")
        try:
            supplier = int(supplier)
            if 1900 <= supplier <= datetime.datetime.now().year:
                break
            else:
                print("Invalid year entered! \n")
        except ValueError:
            print("Invalid year entered! \n")
    while True:
        stock = input("Enter Stock: ")
        try:
            stock = int(stock)
            break
        except ValueError:
            print("Invalid stock entered! \n")
    stationary_dict[prod_id] = Stationary(prod_id, prod_name, category, brand, supplier, stock)
    print("Stationary added successfully! \n")


def display_stationary(records):
    if len(records) == 0:
        print("There are currently no products in the system! \n")
    else:
        print("Product List")
        for value in records:
            print(f"Prod id: {value.get_prod_id()}")
            print(f"Prod Name: {value.get_prod_name()}")
            print(f"Category: {value.get_category()}")
            print(f"Brand: {value.get_brand()}")
            print(f"Supplier Since: {value.get_supplier()}")
            print(f"Stocks: {value.get_stock()}")
            print()  # Empty line for separation


def set_number_of_records_per_row():
    return int(input("Enter number of records per row: "))


def display_records_per_row(records, num_rows=1, current_index=0):
    if not records:
        return

    if current_index >= len(records):
        return

    end_row = min(current_index + num_rows, len(records))

    column_width = 30

    # Header line for Prod id
    for i in range(current_index, end_row):
        record = records[i]
        print(f"{'Prod id:':<15}{record.get_prod_id():<{column_width}}", end="")
    print()

    # Header line for Prod Name
    for i in range(current_index, end_row):
        record = records[i]
        print(f"{'Prod Name:':<15}{record.get_prod_name():<{column_width}}", end="")
    print()

    # Header line for Category
    for i in range(current_index, end_row):
        record = records[i]
        print(f"{'Category:':<15}{record.get_category():<{column_width}}", end="")
    print()

    # Header line for Brand
    for i in range(current_index, end_row):
        record = records[i]
        print(f"{'Brand:':<15}{record.get_brand():<{column_width}}", end="")
    print()

    # Header line for Supplier Since
    for i in range(current_index, end_row):
        record = records[i]
        print(f"{'Supplier Since:':<15}{record.get_supplier():<{column_width}}", end="")
    print()

    # Header line for Stocks
    for i in range(current_index, end_row):
        record = records[i]
        print(f"{'Stocks:':<15}{record.get_stock():<{column_width}}", end="")
    print()

    print("\n")
    display_records_per_row(records, num_rows, end_row)


def populate_data():
    stationary_dict = {}
    items = [
        Stationary("PD1020", "Pastel Art Paper", "Paper", "Faber-Castell", 2021, 2000),
        Stationary("PD1025", "Mars Lumograph Drawing Pencils", "Pencils", "Staedtler", 2022, 320),
        Stationary("PD1015", "Water color Pencils", "Pencils", "Faber-Castell", 2011, 150),
        Stationary("PD1050", "Noris 320 fiber tip pen", "Pens", "Staedtler", 2021, 350),
        Stationary("PD1001", "Copier Paper (A4) 70gsm", "Paper", "PaperOne", 2011, 1500),
        Stationary("PD1033", "Scientific Calculator FX-97SG X", "Calculator", "Casio", 2022, 50),
        Stationary("PD1005", "POP Bazic File Seperator Clear", "Office Supplies", "Popular", 2000, 500)
    ]
    for item in items:
        stationary_dict[item.get_prod_id()] = item
    print("Data populated successfully! \n")
    return stationary_dict


def main_menu():
    global stationary_dict, sorted_list
    stationary_dict = populate_data()
    records_per_row = 1  # Default number of records per row
    while True:
        print("Stationary Management System")
        print("1. Add a new Stationary.")
        print("2. Display all Stationary.")
        print("3. Sort Stationary via Bubble sort on Category.")
        print("4. Sort Stationary via Insertion sort on Brand.")
        print("5. Sort Stationary via Selection sort on Prod id.")
        print("6. Sort Stationary via Merge sort on Category followed by stock in ascending order.")
        print("7. Go to Restocking Menu")
        print("8. Set number of records per row to display")
        print("9. Populate data")
        print("0. Exit Program")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_stationary(stationary_dict)
        elif choice == "2":
            if sorted_list:
                display_records_per_row([item[1] for item in sorted_list], records_per_row)
            else:
                display_records_per_row(list(stationary_dict.values()), records_per_row)
        elif choice == "3":
            sorted_list = bubble_sort_category(stationary_dict, 'category')
            display_records_per_row([item[1] for item in sorted_list], records_per_row)
            print("Stationary sorted via Bubble Sort on Category.")
        elif choice == "4":
            sorted_list = insertion_sort_brand(list(stationary_dict.items()), 'brand')
            display_records_per_row([item[1] for item in sorted_list], records_per_row)
            print("Stationary sorted via Insertion Sort on Brand.")
        elif choice == "5":
            sorted_list = selection_sort_prod_id_desc(stationary_dict)
            display_records_per_row([item[1] for item in sorted_list], records_per_row)
            print("Stationary sorted via Selection Sort on Prod id.")
        elif choice == "6":
            sorted_list = merge_sort(list(stationary_dict.items()), 'category', 'stock')
            display_records_per_row([item[1] for item in sorted_list], records_per_row)
            print("Stationary sorted via Merge Sort on Category followed by stock in ascending order.")
        elif choice == "7":
            restocking_menu(stationary_dict)
        elif choice == "8":
            records_per_row = set_number_of_records_per_row()
        elif choice == "9":
            stationary_dict = populate_data()
            sorted_list = None
        elif choice == "0":
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main_menu()
