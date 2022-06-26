class Mass:
    """
    class Mass with overriding default methods
    """

    print("class Mass")

    value = 0
    unit = 'k'

    map = {
        'g': 1000,
        'k': 1,
        't': 1 / 1000
    }

    def __str__(self):
        return "Mass({} kg)".format(self.value / self.map[self.unit])

    def __float__(self):
        return self.value / self.map[self.unit]

    def __add__(self, other):
        r = Mass()
        r.value = float(self) + float(other)
        return r

    def __iadd__(self, other):
        self.value = float(self) + float(other)
        self.unit = 'k'
        return self


x = Mass()
x.value = 100
x.unit = 'g'

y = Mass()
y.value = 2
y.unit = 'k'

print(x)
print(y)
print(x + y)
x += y
print(x, y)
print(x + y)


# print(x - y) # unsupported operand type(s) for -: 'Mass' and 'Mass'


class Box:
    print("class Box")

    items = [1, 2, 3, 4, 5]

    def __str__(self):
        return "Box({})".format(self.items)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)


b = Box()

for item in b:
    print(item, end=',')


class Dict:
    print("class Dict")

    _data = {}

    def __setitem__(self, name, value):
        self._data[name] = value

    def __getitem__(self, name):
        if name in self._data:
            return self._data[name]

    def __delitem__(self, name):
        del self._data[name]


d = Dict()

d['k'] = 55
print(d['k'])

del d['k']
print(d['k'])


class A:
    print()
    print("class A")

    value = 10

    def __add__(self, other):
        return len(str(self)) + len(str(other))

    def __str__(self):
        return 'A'


class B:
    print("class B")

    value = 20

    def __add__(self, other):
        return self.value + other.value

    def __str__(self):
        return 'B'


print(B() + A())


class C:
    print("class C")

    value = 'hello'

    def __imul__(self, value):
        self.value *= value

    def __str__(self):
        return self.value


ob = C()
ob *= 2

print(ob)


class D:
    print("class D")

    def __add__(self, other):
        return self.i + other.i

    def __radd__(self, other):
        return self.x + other.x


obj = D()
obj.i, obj.x = 1, 2

obj2 = D()
obj2.i, obj2.x = 10, 20

print(obj + obj2)
