# task 1
print('task 1')


# reduce(add, [1, 2, 3, 4]) -> add(add(add(1, 2), 3), 4)

def reduce(func, collection):
    res = 0
    count_add = 0
    count_multiple = 1
    for _ in collection:
        if func is add:
            count_add = func(collection[_ - 1], count_add)
            res = count_add
        else:
            count_multiple = func(collection[_ - 1], count_multiple)
            res = count_multiple
    return res


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


print(reduce(add, range(1, 10)))  # print('45')
print(reduce(mul, range(1, 10)))  # print('362880')

# task 2
print('task 2')


def filterfalse(func, collection):
    result = []
    for _ in collection:
        if not func(_):
            result.append(_)
    return result


text = 'I am an Arm and I sound like U u U u U u U u U'
list_text = list(text)

x = list(filter(lambda i: i.islower(), list_text))
y = list(filterfalse(lambda i: i.islower(), list_text))
print(x)
print(y)

# task 3
print('task 3')

a = [1, 2, 3, 4]
b = ['arm', 'sounds', 'like', 'uUuUuU']


def product(a, b):
    pairs = []
    for i in a:
        for j in b:
            pair = i, j
            pairs.append(pair)
    return pairs


print(product(a, b))
