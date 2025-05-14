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

    @property
    def name(self):
        return self.__name

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        pass

    def __send_body(self):
        pass

    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send_body()
        print("Email sent")

item1 = Item("Item 1", 750)

# ! this gives AttributeError: 'Item' object has no attribute 'send_body'
# item1.send_body()

item1.send_email()


# TODO: read this article
# https://www.datacamp.com/tutorial/python-abstract-classes