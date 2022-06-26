a = 1
b = '2'

try:
    var1 = a + b
except TypeError as e:
    print('"{}" was handled'.format(e.__class__.__name__))
    # except should fix try code

print('Finish')


class EmptyStringError(Exception):
    pass
# we can also create our own exception classes


def reverse(s):
    if len(s) == 0:
        raise EmptyStringError('len(s) == 0')
    return s[::-1]


try:
    print(reverse(" should be reversed"))
except EmptyStringError as e:
    print(e)
