# class User:
#     """
#     ex of how to use int and class object
#     """
#
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#     def __str__(self):
#         return '{} <{}>'.format(self.name, self.email)
#
#
# jane = User('Jane Doe', 'janedoe@example.com')
# print(jane)
#
#
# class Singleton:
#     """
#     __new__ overwrites object behaviour on its creation
#     """
#
#     instance = None
#
#     def __new__(cls):
#         if cls.instance is None:
#             cls.instance = super().__new__(cls)
#
#         return cls.instance
#
#
# # a and b are the same objects, only one instance of this class might be created
# a = Singleton()
# b = Singleton()
#
# var = a is b
# print(var)


class Logger:
    """
    __call__ defines behaviour when our class is calling. On ex define a logger which will be used
    """

    def __init__(self, filename):
        self.filename = filename

    def __call__(self, func):
        with open(self.filename, 'w') as f:
            f.write('Logged')
        return func


logger = Logger('logger.txt')


@logger
def completely_useless_function():
    pass


completely_useless_function()

with open('logger.txt') as f:
    print(f.read())


class PascalList:
    def __init__(self, original_list=None):
        self.container = original_list or []

    def __getitem__(self, index):
        return self.container[index - 1]

    def __setitem__(self, index, value):
        self.container[index - 1] = value

    def __str__(self):
        return self.container.__str__()


numbers = PascalList([1, 2, 3, 4, 5])
print(numbers[1])

numbers[5] = 25
print(numbers)

print(numbers[3])
