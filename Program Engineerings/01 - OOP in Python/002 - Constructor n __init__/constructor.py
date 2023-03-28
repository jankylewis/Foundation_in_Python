class Item:
    # __init__ does in backgr
    # __init plays as constructor role
    def __init__(self, item_name: str, item_price: float, item_quantity: int = 0):
        # validate the received arguments: if not be matched -> throw exceptions with messages
        assert item_price >= 0, f"Price: {item_price} was not greater than 0!"
        assert item_quantity >= 0, f"Quantity: {item_quantity} was not greater than 0!"

        # facilitate dynamically assign an attribute to each instance of creation
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # self is automatically generated because at least 1 parameter is initialized
    def calculate_total_price(self):
        return self.item_price * self.item_quantity


# create instances of the class: instance attributes
item1 = Item("phone", 120, +5)
item2 = Item("laptop", +130, 4)
# ability to add some more specific attribute only having of that item
item2.has_numpad = False

print(f"\nitem name: {item1.item_name}")
print(f"item price: {item1.item_price}")
print(f"item quantity: {item1.item_quantity}")
print(f"item total price: {item1.calculate_total_price()}")
print(f"\nitem name: {item2.item_name}")
print(f"item price: {item2.item_price}")
print(f"item quantity: {item2.item_quantity}")
print(f"item having numpad: {item2.has_numpad}")
print(f"item total price: {item2.calculate_total_price()}")
