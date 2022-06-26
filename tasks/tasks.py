
# task, generator example

def fibonacci(n):
   a = b = 1
   for _ in range(n):
       yield a
       a, b = b, a + b

for num in fibonacci(10):
   print(num)



# task 1, write function which return max from list numbers
import random

task_1 = [1, 4, 99, 0, 6, 22, 11, 7]


def max(ar):
    mx = ar[0]

    for _ in ar:
        if _ > mx:
            mx = _
    return mx


print("task_1:", max(task_1))

# task 2, sum of all elements in the array
task_2 = [8, 0, 5, 7, 19, 20, 11]


def sum(ar):
    sm = 0
    for _ in ar:
        sm = sm + _
    return sm


print("task_2:", sum(task_2))


# task 3, 999 -> 9*9*9 -> 729 -> 7*2*9 -> 126 -> 1*2*6 -> 12 -> 1*2 -> 2, return 4


def mull_numb(number):
    sum = 1
    count = 0
    while len(str(number)) != 1:
        for digit in str(number):
            sum = sum * int(digit)
        number = sum
        sum = 1
        count += 1
    return count


print("task_3:", mull_numb(999))

# task 4, bubble sort
task_4 = [32, 11, 18, 71, 9, 2, 14, 3, 91, 29, 38]


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print("task_4:", bubble_sort(task_4))

# task 5, change key, value to value key for dictionary
task_5 = {1: "hello", 2: "yo", 3: "bye"}


def switch_value_key(d):
    d2 = {}
    for k, v in d.items():
        d2[v] = k
    return d2


print("task_5:", switch_value_key(task_5))

# task 6, list objects in the memory
a = [5, 6]
b = a + []
print("task 6:")
print(a == b, a is b)
print(id(a), id(b))

# task 7, parse string using filter and lambda functions
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"


def clean_up_la(st, char):
    return "".join(filter(lambda x: x != char, st))


def clean_up(st, char):
    char_list = []
    for i in st:
        if i != char:
            char_list.append(i)
    return "".join(char_list)


print("task 7:", clean_up(garbled, 'X'))
print("task 7:", clean_up_la(garbled, 'X'))

# task 8, create a function called flatten that takes a single list and concatenates all the sub lists that
# are part of it into a single list
task_8 = [[1, 2, 3], [4, 5, 6, 7, 8, 9, [99, 10, 98], 10]]


def flatten(ar):
    single_list = []
    for items in ar:
        for item in items:
            single_list.append(item)
    return single_list


print("task 8:", flatten(task_8))

# task 9, find median
task_9 = []
for _ in range(10):
    task_9.append(random.randint(10, 20))

print(task_9)


def find_median(ar):
    ar.sort()
    half_size_len = len(ar) // 2
    return sum(ar[half_size_len - 1: half_size_len + 1]) / 2


print("task 9:", find_median(task_9))

# task 10, find mean
task_10 = []
for _ in range(10):
    task_10.append(random.randint(10, 20))

print(task_10)


def find_mean(ar):
    sm = 0
    for i in ar:
        sm = sm + i
    return sm / len(ar)


print("task 10:", find_mean(task_10))

# task 11, find words qty in sentence

task_11 = "hi, i am an arm and i sound like uUuUuuUU"


def words_counter(st):
    li = st.split(" ")
    return len(li)


print("task 11:", words_counter(task_11))

# task 12, iterate over dict

print("task 12, iterate over dict:")

beatles_map = {
    'Paul': 'Bass',
    'John': 'Guitar',
    'George': 'Guitar',
}

# iterating by keys
print("iterating by keys: ")
for key in beatles_map.keys():
    print(key)

# iterating by keys, values
print("iterating by keys, values: ")
for key, value in beatles_map.items():
    print('{}: {}'.format(key, value))

# iterating by values
print("iterating by values: ")
for value in beatles_map.values():
    print(value)

# task 13, extract values from dict

payments = ['Cash', 'Credit']
summary_table_data = {'Tax': '$0.00', 'Subtotal': '$7.77', 'Discounts': '$0.00', 'Cash': '$6.77', 'Credit': '$2.00'}


def get_payments_data(li):
    all_returned_items = {}
    for key, value in summary_table_data.items():
        if key in li:
            all_returned_items[key] = value
    return all_returned_items


print(f'task 13: {get_payments_data(payments)}')
