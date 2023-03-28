import csv


class Item:
    pay_rate = 0.8  # the pay rate after being discounted by 20%
    # add all our instances to the list
    all = []

    def __init__(self, item_name: str, item_price: float, item_quantity: int = 0):
        # validate the received arguments: if not be matched -> throw exceptions with messages
        assert item_price >= 0, f"Price: {item_price} was not greater than 0!"
        assert item_quantity >= 0, f"Quantity: {item_quantity} was not greater than 0!"

        # facilitate dynamically assign an attribute to each instance of creation
        self.__item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        # actions to execute: when an instance is created -> add that instance into the all []
        Item.all.append(self)

    # property decorator means item_name will be read-only attribute, __ means private attribute
    @property
    def item_name(self):
        return self.__item_name

    @item_name.setter
    def item_name(self, value):
        self.__item_name = value

    def calculate_total_price(self):
        return self.item_price * self.item_quantity

    def apply_discount(self):
        self.item_price = self.item_price * self.pay_rate
        # Item.pay_rate will be class attribute, self.pay_rate will be instance attribute

    @classmethod
    def instantiate_from_csv(cls):
        # r means read, f means file
        with open('items.csv', 'r') as f:
            # directly read the csv file
            reader = csv.DictReader(f)
            # convert to a list
            items = list(reader)
        for item in items:
            Item(
                item_name=item.get('item_name'),
                item_price=float(item.get('item_price')),
                item_quantity=int(item.get('item_quantity')),
            )

    # static method does not receive parameter as a first argument unlikely to class which receives the first argument (self)
    # -> there is no need to have the first argument as self, able to ignore that and put our necessary argument
    @staticmethod
    def is_integer(num):
        # check if the received argument is an instance of a float or an integer
        if isinstance(num, float):
            return False, f"{num} is a float number"
        # elif isinstance(num, float):
        #     # count the float number
        #     return num.is_integer(), f"{num} is a float number with point zero"
        elif isinstance(num, int):
            return True, f"{num} is an integer number"
        else:
            return False

    # after appending all instances to the all [], use the __repr__ constructor to show all the attributes of instances
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.item_name}', {self.item_price}, {self.item_quantity})"
