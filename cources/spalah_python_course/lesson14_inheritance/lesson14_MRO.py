class A:
    name = 'A'


class B(A):
    name = 'B'


class X:
    name = 'X'


class Y(X):
    name = 'Y'


class Main(Y, B):
    pass


o = Main()
print(o.name)

# A X
# B Y
#  M

# with existing realization we search for name value in child: Y, X (right branch) B, A (left branch)

# to check inheritance chain use __mro__
for _ in Main.__mro__:
    print(_)


