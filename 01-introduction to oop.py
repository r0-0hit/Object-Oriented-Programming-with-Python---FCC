item1_name = "Phone"
item1_price = 100
item1_quantity = 5
item1_calculate_total_price = item1_price * item1_quantity


item2_name = "Laptop"
item2_price = 2000
item2_quantity = 3
item2_calculate_total_price = item2_price * item2_quantity


class Item:
    # * In Python, any instance method of a class will, by default, receive the instance (object) as its first parameter, typically named self.

    # def calculate_total_price(self):
    #     return self.price * self.quantity

    def calculate_total_price(self, x, y):
        return x * y


item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))
# print(item1.calculate_total_price())


item2 = Item()
item2.name = "Laptop"
item2.price = 2000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))
# print(item2.calculate_total_price())
