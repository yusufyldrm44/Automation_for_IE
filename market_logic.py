import os
import random
from market_classes import Product, Supplier

class MarketSystem:
    def __init__(self):
        self.product_list = []
        self.cart = []
        self.supplier = Supplier("Central Depot")
        self.total_income = 0
        self.load_data()

    def load_data(self):
        if os.path.exists("market.txt"):
            f = open("market.txt", "r", encoding="utf-8")
            for line in f:
                data = line.strip().split(",")
                if len(data) == 5:
                    p = Product(data[0], data[1], data[2], data[3], data[4])
                    self.product_list.append(p)
            f.close()

    def add_to_cart(self, p_name, qty):
        for p in self.product_list:
            if p.name == p_name:
                if p.stock >= qty:
                    cost = p.price * qty
                    self.cart.append({"product": p, "qty": qty, "cost": cost})
                    return True
        return False

    def manual_add_stock(self, p_name, qty):
        for p in self.product_list:
            if p.name == p_name:
                p.add_stock(qty)
                return True
        return False

    def checkout_step1(self):
        log = ""
        for item in self.cart:
            p = item["product"]
            q = item["qty"]
            p.sell_product(q)
            self.total_income += item["cost"]
            log += f"- {p.name}: {q} sold.\n"
        self.cart = []
        return log

    def check_auto_order_step2(self):
        log = ""
        flag = False
        for p in self.product_list:
            if p.stock <= p.threshold:
                amt = self.supplier.send_shipment(p)
                log += f"Low stock: {p.name}. Added {amt}.\n"
                flag = True
        return flag, log

    def simulate_step(self):
        if len(self.product_list) > 0:
            p = random.choice(self.product_list)
            q = random.randint(1, 5)
            if p.sell_product(q):
                self.total_income += p.price * q
            if p.stock <= p.threshold:
                self.supplier.send_shipment(p)

    def get_report(self):
        rep = "--- MONTHLY REPORT ---\n\n"
        rep += f"Total Revenue: {self.total_income:.2f}\n"
        rep += "Inventory Status:\n"
        for p in self.product_list:
            st = "Normal"
            if p.stock <= p.threshold: st = "CRITICAL"
            elif p.stock > p.threshold * 2: st = "High"
            rep += f"- {p.name} : {p.stock} [{st}]\n"
        return rep