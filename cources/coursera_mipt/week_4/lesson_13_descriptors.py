class ImportantValue:
    """
    Class to define set and get behaviour, write value into file each time when use object
    """

    def __init__(self, amount):
        self.amount = amount

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        with open('descriptors_log.txt', 'w') as f:
            f.write(str(value))

        self.amount = value


class Account:
    """
    Class to operate with changed class and object
    """

    amount = ImportantValue(100)


my_account = Account()
sam_account = Account()

my_account.amount = 150

with open('descriptors_log.txt', 'r') as f:
    print(f.read)
