class Counter:
    """
    class Counter counts all elements of the collection and return it as dict
    """
    print('class Counter')

    f_dict = {}

    def __str__(self):
        return str(self.f_dict)

    def update(self, text):
        d = dict.fromkeys(text, 0)
        for char in text:
            d[char] += 1
        self.f_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))


c = Counter()
c.update('I am an arm, and I sound like this')
print(c)


class Point:
    """
    class Point represent point on x, y axis, coordinates are callable by name or by index
    """
    print('class Point')

    points = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.points.append(x)
        self.points.append(y)

    def __getitem__(self, i):
        return self.points[i]


p = Point(1, 2)
print(p[0], p[1])
print(p.x, p.y)


class ChainMap:
    """
    class ChainMap group key : [values] from any dicts number
    """
    print('class ChainMap')

    super_dict = {}

    def __init__(self, *args):
        for d in args:
            for k, v in d.items():
                self.super_dict.setdefault(k, []).append(v)

    def __getitem__(self, i):
        dict_list = self.super_dict[i]
        return dict_list[0]


d = ChainMap({'a': 1}, {'a': 2, 'b': 3}, {'a': 10, 'b': 20, 'c': 30})
print(d.super_dict)
print(d['a'], d['b'], d['c'])


class LikeString(str):
    """
    class LikeString is a like string class but you can change the string by index
    """
    print('class LikeString')

    def __init__(self, text):
        super().__init__()
        self.text = list(text)

    def __str__(self):
        return "".join(self.text)

    def __setitem__(self, i, val):
        self.text[i] = val


a = LikeString('hello')
a[4] = ' Arm'
print(a)
