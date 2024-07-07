class Stationary:
    def __init__(self, prod_id, prod_name, category, brand, supplier):
        self.Prod_id = prod_id
        self.ProdName = prod_name
        self.Category = category
        self.Brand = brand
        self.Supplier = supplier
    
    def get_prod_id(self):
        return self.Prod_id
    
    def get_prod_name(self):
        return self.ProdName
    
    def get_category(self):
        return self.Category
    
    def get_brand(self):
        return self.Brand
    
    def get_supplier(self):
        return self.Supplier
    
    def set_prod_id(self, prod_id):
        self.Prod_id = prod_id

    def set_prod_name(self, prod_name):
        self.ProdName = prod_name
        
    def set_category(self, category):
        self.Category = category

    def set_brand(self, brand):
        self.Brand = brand

    def set_supplier(self, supplier):
        self.Supplier = supplier
