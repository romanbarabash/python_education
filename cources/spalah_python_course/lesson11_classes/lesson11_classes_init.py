class A:

    """
    In this example - when modify A.x we do not overwrite values in o object of class A, because of using init
    hasattr(obj, property) - checks if object has exact property
    getattr(obj, property, default) - get value of property of object or return default
    setattr(obj, property, value) - set new property and value for object
    """

    def init(self):
        self.x = 0

    def to_str(self):
        return 'A(x={})'.format(self.x)


o = A()
o.init()

A.x = 1000

print(o.to_str())
print(o.x)

print(hasattr(o, 'x'))
print(getattr(o, 'y', 666))
setattr(o, 'y', 777)
print(getattr(o, 'y', 666))
