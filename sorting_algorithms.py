# Kaushik, 233050P, IT2153, Assignment 2

def bubble_sort_category(my_dict, key_to_sort):
    items = list(my_dict.items())
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if getattr(items[j][1], key_to_sort) > getattr(items[j + 1][1], key_to_sort):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        print(f"Pass {i + 1}:")
        print("-----------------------------------")
        for key, _ in items:
            print("Prod_id:", key)
        print("-----------------------------------")
        if not swapped:
            break
    return items


def insertion_sort_brand(items, key_to_sort):
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and getattr(key[1], key_to_sort) < getattr(items[j][1], key_to_sort):
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key
        print(f"Pass {i}:")
        print("-----------------------------------")
        for k, _ in items:
            print("Prod_id:", k)
        print("-----------------------------------")
    return items


def selection_sort_prod_id_desc(my_dict):
    items = list(my_dict.items())
    for i in range(len(items)):
        max_idx = i
        for j in range(i + 1, len(items)):
            if items[j][1].get_prod_id() > items[max_idx][1].get_prod_id():
                max_idx = j
        items[i], items[max_idx] = items[max_idx], items[i]
        print(f"Pass {i + 1}:")
        print("-----------------------------------")
        for key, _ in items:
            print("Prod_id:", key)
        print("-----------------------------------")
    return items


def merge_sort(items, key_to_sort, secondary_key):
    if len(items) > 1:
        mid = len(items) // 2
        left_half = items[:mid]
        right_half = items[mid:]

        merge_sort(left_half, key_to_sort, secondary_key)
        merge_sort(right_half, key_to_sort, secondary_key)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if (getattr(left_half[i][1], key_to_sort), getattr(left_half[i][1], secondary_key)) < (getattr(right_half[j][1], key_to_sort), getattr(right_half[j][1], secondary_key)):
                items[k] = left_half[i]
                i += 1
            else:
                items[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            items[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            items[k] = right_half[j]
            j += 1
            k += 1

    print("-----------------------------------")
    for key, _ in items:
        print("Prod_id:", key)
    print("-----------------------------------")
    return items
