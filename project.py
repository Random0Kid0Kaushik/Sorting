# Import the Stationary class from stationary.py
from stationary import Stationary
# import datetime module
import datetime

# Create a list of stationary objects
stationary_dict = {}

# Variables to store sorted lists
bubble_sorted_list = None
insertion_sorted_list = None


def populate_data():
    stationary_dict = {}
    item = Stationary("PD1020", "Pastel Art Paper", "Paper", "Faber-Castell", 2021)
    stationary_dict[item.get_prod_id()] = item
    item = Stationary("PD1025", "Mars Lumograph Drawing Pencils", "Pencils", "Staedtler", 2022)
    stationary_dict[item.get_prod_id()] = item
    item = Stationary("PD1015", "Water color Pencils", "Pencils", "Faber-Castell", 2011)
    stationary_dict[item.get_prod_id()] = item
    item = Stationary("PD1050", "Noris 320 fiber tip pen", "Pens", "Staedtler", 2021)
    stationary_dict[item.get_prod_id()] = item
    item = Stationary("PD1001", "Copier Paper (A4) 70gsm", "Paper", "PaperOne", 2011)
    stationary_dict[item.get_prod_id()] = item
    item = Stationary("PD1033", "Scientific Calculator FX-97SG X", "Calculator", "Casio", 2022)
    stationary_dict[item.get_prod_id()] = item
    item = Stationary("PD1005", "POP Bazic File Seperator Clear", "Office Supplies", "Popular", 2000)
    stationary_dict[item.get_prod_id()] = item
    print("Data populated successfully! \n")
    return stationary_dict


def bubble_sort_category(my_dict, key_to_sort):
    items = list(my_dict.items())  # Convert to list of (key, value) tuples

    for i in range(len(items) - 1):  # Iterate through the list to sort
        print(f"Pass: {i + 1}")  # Print pass number
        print("-----------------------------------")
        swapped = False  # Flag to track if any swaps occurred in a pass
        for j in range(len(items) - 1 - i):  # Iterate through the list and compare adjacent elements
            # Access the attribute using getattr
            if getattr(items[j][1], key_to_sort) > getattr(items[j + 1][1], key_to_sort):
                items[j], items[j + 1] = items[j + 1], items[j]  # Swap the elements if they are in the wrong order
                swapped = True  # Set the swapped flag to True

        # Print Prod_id after each pass
        for key, _ in items:
            print("Prod_id:", key)
        print("-----------------------------------")

        if not swapped:  # If no swaps occurred, the list is sorted
            break

    return items


def insertion_sort_brand(items, key_to_sort):
    # Start from the second element in the list
    for i in range(1, len(items)):  # Iterate through the list
        key = items[i]  # Get the key at the current index
        j = i - 1  # Set the index of the previous element

        # Comparison using getattr to get the attribute value
        while j >= 0 and getattr(key[1], key_to_sort) < getattr(items[j][1], key_to_sort):
            items[j + 1] = items[j]  # Move the element to the right if it is greater than the key
            j -= 1  # Move to the previous element in the list if the key is smaller

        items[j + 1] = key  # Insert the key at the correct position in the list

        print(f"Pass {i}:")  # Print pass number
        print("-----------------------------------")
        for k, _ in items:  # Print Prod_id after each pass
            print("Prod_id:", k)
        print("-----------------------------------")

    return items


def add_stationary():
    while True:  # Keep asking for input until valid input is provided
        prod_id = input("Enter Product ID: ")

        # Validate if the product ID already exists
        if prod_id in stationary_dict:
            print("Product ID already exists! \n")
            continue  # Ask for product ID again
        else:
            break  # Valid product ID, exit the loop

    prod_name = input("Enter Product Name: ")
    category = input("Enter Product Category: ")
    brand = input("Enter Brand: ")

    while True:  # Keep asking for input until valid input is provided
        supplier = input("Please enter the year this supplier started supplying this product: ")

        # Validate if the year is a number
        try:
            supplier = int(supplier)
            break  # Valid year, exit the loop
        except ValueError:
            print("Invalid year entered! \n")
        # Validate if the number is within the range of years (1900 - current year)
            if supplier < 1900 or supplier > datetime.datetime.now().year:
                print("Invalid year entered! \n")
            else:
                break

    # Create a new Stationary object and add it to the dictionary
    stationary_dict[prod_id] = Stationary(prod_id, prod_name, category, brand, supplier)
    print("Stationary added successfully! \n")


def display_stationary():
    if len(stationary_dict) == 0:
        print("There are currently no products in the system! \n")
    else:
        print("Product List")
        for value in stationary_dict.values():
            print("-----------------------------------")
            print("Product ID: ", value.get_prod_id())
            print("Product Name: ", value.get_prod_name())
            print("Category: ", value.get_category())
            print("Brand: ", value.get_brand())
            print("Supplier Since: ", value.get_supplier())


while True:
    try:
        print("Stationary_Management System")
        print("1. Add a new Stationary")
        print("2. Display all Stationary")
        print("3. Sort Stationary via Bubble sort on Category")
        print("4. Sort Stationary via Insertion sort on Brand")
        print("9. Populate data")
        print("0. Exit")
        choice = int(input("Please select one: "))
        if choice == 1:
            add_stationary()
        elif choice == 2:
            display_stationary()
        elif choice == 3:
            # Bubble sort on Category
            bubble_sorted_list = bubble_sort_category(stationary_dict.copy(), "category")
            print("-----------------------------------")
            print("\n")
            print("Product List")
            for key, value in bubble_sorted_list:
                print("-----------------------------------")
                print(f"Product ID: {value.get_prod_id()}")
                print(f"Product Name: {value.get_prod_name()}")
                print(f"Product Category: {value.get_category()}")
                print(f"Brand: {value.get_brand()}")
                print(f"Supplier Year: {value.get_supplier()}")

        elif choice == 4:
            # Insertion sort (using the Bubble Sorted list if available)
            if bubble_sorted_list is not None:  # Check if Bubble Sort has been performed
                insertion_sorted_list = insertion_sort_brand(bubble_sorted_list.copy(), "Brand")  # Sort the Bubble Sorted list
            else:
                insertion_sorted_list = insertion_sort_brand(list(stationary_dict.items()).copy(), "Brand")  # Sort the original list

            print("-----------------------------------")
            print("\n")
            print("Product List")
            for key, value in insertion_sorted_list:
                print("-----------------------------------")
                print(f"Product ID: {value.get_prod_id()}")
                print(f"Product Name: {value.get_prod_name()}")
                print(f"Product Category: {value.get_category()}")
                print(f"Brand: {value.get_brand()}")
                print(f"Supplier Year: {value.get_supplier()}")

        elif choice == 9:
            stationary_dict = populate_data()
        elif choice == 0:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid choice! Please enter a number")
    except Exception as e:
        print("An error occurred: ", e)
