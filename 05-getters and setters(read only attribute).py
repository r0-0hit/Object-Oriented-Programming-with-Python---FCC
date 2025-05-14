class Item:

    pay_rate = 0.8 # the pay rate after discount of 20%
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # * do like this to follow SOLID principles
        # validation of received arguments
        self.validate_attributes(price, quantity)

        # assign to self-obj
        self.__name = name
        self.price = price
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
        return f"{self.__class__.__name__}({self.name}, {self.price},{self.quantity})"

    # Property Decorator = read-only attribute
    @property
    def read_only_name(self):
        return "AAA"

    # ! this will convert name attribute to read-only.
    # ! so will cause error in __init__ where we are self.name = name, so to resolve it we use "_" prefix for the attribute
    # ! but it allows "item1._name = "OtherName", to resolve this "__" prefix is used for attributes
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

# * set attribute "name" ot read-only
item1 = Item("Laptop", 1000, 3)

# * this is allowed in normal, but I want so that I cannot change it. I will do this by using @property
# item1.name = "OtherName"

# * This will give "AttributeError: property 'read_only_name' of 'Item' object has no setter" error
# item1.read_only_name = "BBB"

# after @property def name
print(item1.name)

# ! this will give error
# item1.name = "OtherName"

# ? look why does it allow this
# item1._name = "OtherName"

# * this will not work because below
# item1.__name = "OtherName"

# ! AttributeError: 'Item' object has no attribute '__name'. Did you mean: 'name'?
# print(item1.__name)

# TODO:
# | Prefix    | Access Type    | Name Mangling?  | Purpose                      |
# | --------- | -------------- | --------------- | ---------------------------- |
# | `_var`    | Protected-ish  | ❌ No           | Internal use (by convention) |
# | `__var`   | Private-ish    | ✅ Yes          | Avoid accidental access      |
# | `__var__` | Special Method | ❌ No           | Reserved (e.g., `__init__`)  |

# ? WTF??
# In Python, the use of private and protected is more about convention than enforced access control, as the language relies heavily on the "we're all-consenting adults" philosophy, trusting programmers to respect these conventions.

# 🔍 What is Name Mangling?
# When you define a class attribute with two leading underscores (e.g., __private_var), Python renames it internally by prefixing it with _ClassName, to avoid accidental access or overriding.
# This doesn't make it truly private — it's just obfuscated, not inaccessible.