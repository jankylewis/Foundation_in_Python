class Item:
    pay_rate = 0.8  # the pay rate after being discounted by 20%
    # add all our instances to the list
    all = []

    def __init__(self, item_name: str, item_price: float, item_quantity: int = 0):
        # validate the received arguments: if not be matched -> throw exceptions with messages
        assert item_price >= 0, f"Price: {item_price} was not greater than 0!"
        assert item_quantity >= 0, f"Quantity: {item_quantity} was not greater than 0!"

        # facilitate dynamically assign an attribute to each instance of creation
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        # actions to execute: when an instance is created -> add that instance into the all []
        Item.all.append(self)

    def calculate_total_price(self):
        return self.item_price * self.item_quantity

    def apply_discount(self):
        self.item_price = self.item_price * self.pay_rate
        # Item.pay_rate will be class attribute, self.pay_rate will be instance attribute

    # after appending all instances to the all [], use the __repr__ constructor to show all the attributes of instances
    def __repr__(self):
        return f"Item('{self.item_name}', {self.item_price}, {self.item_quantity})"


item1 = Item("phone", 100, 1)
item2 = Item("laptop", 1000, 3)
item3 = Item("cable", 10, 5)
item4 = Item("mouse", 50, 5)
item5 = Item("keyboard", 75, 5)

print(Item.all)

# for instance in Item.all:
#     print(instance.item_name)

# print(Item.__dict__)  # export all the attributes for Class level
# print("\r")
# print(item1.__dict__)  # export all the attributes for instance level
