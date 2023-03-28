class Item:
    # self is automatically generated because at least 1 parameter is initialized
    # self is always worked in the backgr
    # python passes the first argument
    def calculate_total_price(self, item_price, item_quantity):
        return item_price * item_quantity


# create an instance of the class
item1 = Item()
# random_str = str("4")
# create attributes of class by hard-coding
item1.name = "phone"
item1.price = 120
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

# create attributes of class by hard-coding
item2 = Item()
item2.name = "laptop"
item2.price = 130
item2.quantity = 4
print(item2.calculate_total_price(item2.price, item2.quantity))

# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))
