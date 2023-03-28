from item import Item


class Phone(Item):

    def __init__(self, item_name: str, item_price: float, item_quantity: int = 0, broken_phones: int = 0):
        # call to super function to have the full access to all attributes and methods of the parent class
        super().__init__(
            item_name, item_price, item_quantity
        )
        assert broken_phones >= 0, f"Broken phones: {broken_phones} was not greater than 0!"
        self.broken_phones = broken_phones
