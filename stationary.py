# Kaushik, 233050P, IT2153, Assignment 2

# Stationary class to store stationary product details

class Stationary:
    def __init__(self, prod_id, prod_name, category, brand, supplier, stock):
        self.prod_id = prod_id
        self.prod_name = prod_name
        self.category = category
        self.brand = brand
        self.supplier = supplier
        self.stock = stock

    def get_prod_id(self):
        return self.prod_id

    def set_prod_id(self, prod_id):
        self.prod_id = prod_id

    def get_prod_name(self):
        return self.prod_name

    def set_prod_name(self, prod_name):
        self.prod_name = prod_name

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_supplier(self):
        return self.supplier

    def set_supplier(self, supplier):
        self.supplier = supplier

    def get_stock(self):
        return self.stock

    def set_stock(self, stock):
        self.stock = stock
