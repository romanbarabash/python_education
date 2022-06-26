class A:
    items = []

    def __init__(self, name):
        self.name = name
        self.items.append(self.name)

    def __iter__(self):
        return iter(self.items)


x = A('x')
y = A('y')
z = A('z')

for obj in x:
    print(obj)


class B:
    name = None

    def __init__(self, name):
        self.name = name

    def __mul__(self, other):
        return str(self.name + " ") * other


ob = B('object')
result = ob * 5
print(result)


class Range:
    r_list = []

    def __init__(self, n):
        for item in range(0, n + 1):
            self.r_list.append(item)

    def __iter__(self):
        return iter(self.r_list)


x = Range(7)
for i in x:
    print(i)


class MyList:
    your_list_name = []

    def __str__(self):
        return str(self.your_list_name)

    def __len__(self):
        return len(self.your_list_name)

    def __getitem__(self, i):
        return self.your_list_name[i]

    def __setitem__(self, i, val):
        self.your_list_name[i] = val

    def __delitem__(self, i):
        del self.your_list_name[i]

    def append(self, value):
        self.your_list_name.append(value)

    def insert(self, position, value):
        self.your_list_name.insert(position, value)


ob = MyList()
print(ob)

ob.append(1)
ob.insert(0, 2)
print(ob)  # [2, 1]
print(ob[::-1])  # [1, 2]


class City:

    def __init__(self, name, pleace):
        """
        defines how our object will looks like
        """
        self.name = name
        self.pleace = pleace

    def __add__(self, other):
        """
        defines the way we will use + to add our oblects,
        w/o this method will be unsupported operand type(s) for +: 'City' and 'City'
        """
        return str(self) + str(other)

    def __str__(self):
        """
        defines behaviour of printing object of the class
        """
        return "Localization: {}, {}; ".format(self.name, self.pleace)


s = City('Twin peaks', 'WA')
print(s)

d = City('Neverland', 'OH')
print(d)

print(s + d)
