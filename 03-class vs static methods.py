import csv


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

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv") as csv_file:
            reader = csv.DictReader(csv_file)
            items = list(reader)

            for item in items:
                Item(name=item["name"], price=float(item["price"]), quantity=int(item["quantity"]))

    @staticmethod
    def is_integer_idk(num):
        # we will count out floats that are point zero Ex. 10.0, 7.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"Item({self.name}, {self.price},{self.quantity})"


# Item.instantiate_from_csv()
# print(Item.all)

print(Item.is_integer_idk(1.0))