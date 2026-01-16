class Product:
    def __init__(self, name, stock, price, threshold, order_qty):
        self.name = name
        self.stock = int(stock)
        self.price = float(price)
        self.threshold = int(threshold)
        self.order_qty = int(order_qty)
        self.history = [int(stock)] 

    def sell_product(self, amount):
        if self.stock >= amount:
            self.stock -= amount
            self.history.append(self.stock)
            return True
        else:
            return False

    def add_stock(self, amount):
        self.stock += amount
        self.history.append(self.stock)

class Supplier:
    def __init__(self, name):
        self.name = name
    def send_shipment(self, product):
        product.add_stock(product.order_qty)
        return product.order_qty