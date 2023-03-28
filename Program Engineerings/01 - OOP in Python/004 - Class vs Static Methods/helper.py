# the main difference between static and class method is:
#     class method passes the object reference as the first argument
#     static method does not need to pass the first argument -> be able to input the first desired argument
#
# when to use static methods?
#     static method is the method somehow related to the class. Using static method does NOT for purpose of instantiate
#     object (sth that must be unique per instance)

# when to use class methods?
#     class method is the method somehow related to the class. Class methods are usually used to manipulate structured data
#     to instantiate objects, like retrieving data from CSV file

class Item:
    @staticmethod
    def is_integer():
        pass

    @classmethod
    def instantiate_sth(cls):
        pass


# however we can call those methods by CLASS level or INSTANCE level
item1 = Item()
Item.is_integer()
item1.is_integer()
Item.instantiate_sth()
item1.instantiate_sth()
