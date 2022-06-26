"""
Tuple is a list which cannot be modified
"""

"""Сreate tuple"""

o = ()
print(type(o))

a = (1, 1, 2, 3, 4, 5, '5')
print(type(a))

z = ['i', 'a', 'm', 'a', 'n', 'a', 'r', 'm']
b = tuple(z)
print(type(b))

print("""Methods""")

indx = a.index(5)
print(indx)

count = a.count(1)
print(count)

print("""Operations""")
c = a + b
print(c)  # we can add tuples

for _ in c:
    print(_, end=' ')
print()


def return_2_val(tuple):
    return tuple[0], tuple[1]


a, b = return_2_val(a)  # unpack values from function into variables
print(a, b)

a, b, *c = 'I am an arm'  # pack values to a and b and list to c
print(a)
print(b)
print(c)

print("""Change places for variables using tuples and w/o tuples""")

a = 666
b = 13

a = a + b
b = a - b
a = a - b

print(a)
print(b)

z = 33
x = 23

z, x = x, z

print(z)
print(x)

print("""Modification is not  available""")

# a[0] = 0  # this will result error: 'tuple' object does not support item assignment
