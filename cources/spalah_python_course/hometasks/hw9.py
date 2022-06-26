counter = 0


def replace(string, from_, to_):
    splited = string.split(from_)
    return to_.join(splited)


print(replace('hello world', 'l', 'L'))
print(replace('hello world', 'll', 'L'))
print(replace('hello world', 'hello', 'Bye'))
print(replace('hello world', ' ', '-'))


def sort(col):
    i = 0
    while i < len(col) - 1:
        j = 0
        while j < len(col) - 1 - i:
            if col[j] > col[j + 1]:
                col[j], col[j + 1] = col[j + 1], col[j]
            j += 1
        i += 1

    return col


a = [7, 8, 1, 5, 3, 4, 2, 0, 9, 6]
print(sort(a))


def sum(a, b):
    c = a + b
    global counter
    counter += 1
    return "[#{}]: {} + {} = {}".format(counter, a, b, c)


print(sum(10, 27))
print(sum(12, 23))


def lowest_pair(col):
    first = 0
    second = 1

    i = 0
    while i < len(col) - 1:
        j = 0
        while j < len(col) - 1 - i:
            if col[j] > col[j + 1]:
                col[j], col[j + 1] = col[j + 1], col[j]
            j += 1
        i += 1

    return col[first], col[second]


b = [3, 100, 27, 1, 4, 500, 501]
print(lowest_pair(b))
