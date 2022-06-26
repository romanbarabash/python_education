class Point:

    def init(self, x=0, y=0):
        self.x = x
        self.y = y
        self.history = []

    def back(self):
        self.x, self.y = self.history.pop()

    def to_str(self):
        return 'Point({}, {})'.format(self.x, self.y)

    def move(self, delta_x=0, delta_y=0):
        self.history.append([self.x, self.y])
        self.x += delta_x
        self.y += delta_y

    def over(self, obj):
        return self.y > obj.y

    def after(self, obj):
        return self.x > obj.x


a = Point()
a.init(6, 3)
print(a.to_str())

a.move(2, -4)
print(a.to_str())

a.move(-5, 8)
print(a.to_str())

a.back()
print(a.to_str())

b = Point()
b.init()
print(b.to_str())
