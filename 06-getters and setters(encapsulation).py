class Item:
    pay_rate = 0.8  # the pay rate after discount of 20%
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # * do like this to follow SOLID principles
        # validation of received arguments
        self.validate_attributes(price, quantity)

        # assign to self-obj
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # add instances to all lists
        self.add_instance_to_all()

    @staticmethod
    def validate_attributes(price, quantity):
        """validation of received arguments"""
        assert price >= 0, f"Price {price}, should be grater than zero!"
        assert quantity >= 0, f"Quantity {quantity}, should be grater than zero!"

    def add_instance_to_all(self):
        """add instances to all lists"""
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.__price},{self.quantity})"

    # * getter
    @property
    def name(self):
        return self.__name

    # * setter
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    def apply_discount(self, discount=.15):
        self.__price = self.__price - self.__price * discount

    def apply_increase(self, increase):
        self.__price = self.__price + self.__price * increase


item1 = Item("Item 1", 750)

print(item1.name)
item1.name = "Other name"
print(item1.name)

print(item1.price)
item1.apply_increase(.2)
print(item1.price)
item1.apply_discount()
print(item1.price)
