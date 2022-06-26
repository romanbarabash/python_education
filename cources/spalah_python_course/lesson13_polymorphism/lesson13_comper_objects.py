class Number:

    """
    Compare objects methods
    if we do not have __eq__, x == y is False, since objects with equal values are not equal in Python
    if we have __eq__ realization as is, x == y is True
    above relates to __gt__ , __ge__ methods which won't work w/o current realization
    """

    def __init__(self, value):
        self.value = value

    def __eq__(self, object):
        return self.value == object.value

    # eq => ne

    def __gt__(self, object):
        return self.value > object.value

    def __ge__(self, object):
        return self.value >= object.value


x = Number(10)
y = Number(20)
z = Number(10)

print(x == y)
print(x == z)

print(x > z)
print(x >= z)
