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
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price},{self.quantity})"


class Phone(Item):
    # * you don't have to declare all in child class
    # all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # TODO: check it
        # Item.__init__(self, name, price, quantity)
        super().__init__(name, price, quantity)

        assert broken_phones >= 0, f"Broken phones {broken_phones}, should be grater than zero!"

        self.broken_phones = broken_phones

        # Phone.all.append(self)

phone1 = Phone("Phone1", 100, 5, 1)
phone2 = Phone("Phone2", 300, 3, 1)

item1 = Item("Laptop", 1000, 3)

print(Item.all)
print(Phone.all)
phone2.apply_discount()
print(phone2.price)