class A:
    x = 0

    def __str__(self):
        return "A(x={})".format(self.x)

    def get_type(self):
        return type(self)

    def x_gt_zero(self):
        return self.x > 0


class B(A):
    y = 1

    def __str__(self):
        return "B(x={} y={})".format(self.x, self.y)


class C(B):
    z = None

    def __str__(self):
        class_name = self.__class__.__name__
        return "{}(x={} y={} z={})".format(class_name, self.x, self.y, self.z)


class C1(C):
    z = 2


class C2(C):
    z = 30


o1 = A()
o2 = B()
o3 = C1()
o4 = C2()

print(o1.get_type(), o2.get_type())
print(o2)
print(o3)
print(o4)
