from functools import reduce

"""High level functions"""

a = list((range(1, 20)))


def select(collection, is_suitable):
    result = []
    for _ in collection:
        if is_suitable(_):
            result.append(_)
    return result


def check_int_instance(collection, int):
    for _ in collection:
        if not int(_):
            return False
    return True


def convert(collection, convertor):
    result = []
    for _ in collection:
        result.append(convertor(_))
    return result


result = select(a, lambda item: item > 10)
print(result)

result = select(a, lambda item: item % 5 == 0)
print(result)

result = check_int_instance(a, lambda item: isinstance(item, int))
print(result)

result = convert(a, lambda item: str(item))
print(result)

print()
print("""Unpack function arguments""")


# *b means we can set any number of variables into function, which will be considered as tuple
def func(a, *b):
    print(a, b)
    print(type(a))
    print(type(b))


func(1, 2, 3, 4, 6, '666')


# *d means we can set any number of named variables into function, which will be considered as dictionary
def full_var_list(a, *b, c, **d):
    print(a, b, c, d)
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))


full_var_list(1, 2, 3, 4, 5, 6, 7, 8, c='i am an arm', term=25, sounds='UuuuuUUuuu', location='lodge')

print()
print("Built in functions")

# all(collection) -> check_all, checks if all elements return True
# any(collection) -> check_any, checks if any of element return True
# map(function, collection) -> modifies 'collection' relatively to 'function' condition
# filter(function, collection) -> select(filter) items from 'collection' relatively to 'function' condition
# reduce(function, collection) -> apply 'function' to 'collection' elements, summarizing it into one value

col = []
for item in range(1, 10):
    col.append(item > 1)

print(all(col))
print(any(col))

res_map = map(lambda i: i * i, range(1, 10))
for _ in res_map:
    print(_, end=' ')

print()

res_filter = filter(lambda i: i % 5 == 0, range(1, 20))
for _ in res_filter:
    print(_, end=' ')

print()

list_x = list(range(1, 10))

# convert to True, False list and than checks if all is True -> result: False
res = all(map(lambda i: i % 2, list_x))
print(res)

#
red = list((range(1, 10)))
reduced = reduce(lambda el_prev, el: el_prev + el, red)
print("reduced: ", reduced)

# sort the list by 1st element of each tuple
a = [(1, 2), (3, 1), (5, 10), (11, -3)]
a.sort(key=lambda x: x[0])
print(a)

# use lambda functions in dictionary for manipulating with the list
a4 = {'pos': lambda x: x * 2, 'neg': lambda x: abs(x), 'zero': lambda x: float(x)}
b = [-3, 10, 0, 1]
for i in b:
    if i < 0:
        print(a4['neg'](i))
    elif i > 0:
        print(a4['pos'](i))
    else:
        print(a4['zero'](i))
