class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0 

    def add_item(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product,quantity))
            self.total += product.price * quantity
            product.stock -= quantity
            return True
        return False
