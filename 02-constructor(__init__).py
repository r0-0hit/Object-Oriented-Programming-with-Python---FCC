class Item:

    pay_rate = 0.8 # the pay rate after discount of 20%
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # validation of received arguments
        assert price >= 0, f"Price {price}, should be grater than zero!"
        assert quantity >= 0, f"Quantity {quantity}, should be grater than zero!"

        # assign to self obj
        self.name = name
        self.price = price
        self.quantity = quantity

        # add instances to all list
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate # ! don't use Item.pay_rate as if u assign a custom value it will not apply

    def __repr__(self):
        return f"Item({self.name}, {self.price},{self.quantity})"
        #return f"Item: {self.name}, price: {self.price}, quantity: {self.quantity}"

item1 = Item("Phone", 100)
# print(item1.calculate_total_price())


item2 = Item("Laptop", 1000, 3)
# * can also assign custom attributes
#item2.has_numpad = True
# print(item2.has_numpad)
# print(item2.calculate_total_price())

# * even if the obj(instance) does not have that attribute it goes to class and check for the attribute
# print(item1.pay_rate)


"""
    The __dict__ attribute in Python is a special dictionary that stores an object’s (or class’s) writable attributes.
    
    For objects:
    object.__dict__ contains all the instance variables of that object.
    
    For classes:
    ClassName.__dict__ contains class attributes, including methods and other class-level definitions (but as mappings, not bound methods).
"""
# print(Item.__dict__)
# print(item1.__dict__)
# print(item2.__dict__)

item2.pay_rate = 0.7
item2.apply_discount()
item1.apply_discount()
# print(item1.price) # 80.0
# print(item2.price) # 700.0


# More items
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

# * [<__main__.Item object at 0x00000236EEAC1940>, <__main__.Item object at 0x00000236EED3F750>, ...] this will be the output before using __repr__ method

"""
    The __repr__ method in Python is a special method used to define the “official” string representation of an object.
    🔹 Purpose:
    To return a string that unambiguously describes the object.
    
    Ideally, the string should be valid Python code that could recreate the object (if possible).
"""

