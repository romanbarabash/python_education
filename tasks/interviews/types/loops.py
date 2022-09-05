# task 1, generator example
import random

print("_" * 100)


def fibonacci(n):
    a = b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print('task_1: ')
for num in fibonacci(10):
    print(num)

# task 2, write function which return max from list numbers
print("_" * 100)
task_2 = [1, 4, 99, 0, 6, 22, 11, 7]


def max(arr):
    max_value = arr[0]

    for element in arr:
        if element > max_value:
            max_value = element
    return max_value


print("task_2:", max(task_2))

# task 3, sum of all elements in the array
print("_" * 100)
task_3 = [8, 0, 5, 7, 19, 20, 11]


def sum(ar):
    sm = 0
    for i in ar:
        sm = sm + i
    return sm


print("task_3:", sum(task_3))

# task 4, 999 -> 9*9*9 -> 729 -> 7*2*9 -> 126 -> 1*2*6 -> 12 -> 1*2 -> 2, return 4
print("_" * 100)


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


print("task_4:", mull_numb(999))

# task 5, bubble sort
print("_" * 100)
task_5 = [32, 11, 18, 71, 9, 2, 14, 3, 91, 29, 38]


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print("task_5:", bubble_sort(task_5))

# task 6, parse string using filter and lambda functions
print("_" * 100)
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"


def clean_up_lambda(st, char):
    return "".join(filter(lambda x: x != char, st))


def clean_up(char, st):
    char_list = []
    for i in st:
        if i != char:
            char_list.append(i)
    return "".join(char_list)


print("task 6:", clean_up(garbled, 'X'))
print("task 6:", clean_up_lambda(garbled, 'X'))

# task 7, create a function called flatten that takes a single list and concatenates all the sub lists that are part of it into a single list
print("_" * 100)
task_7 = [[1, 2, 3], [4, 5, 6, 7, 8, 9, [99, 10, 98], 10]]


def flatten(ar):
    single_list = []
    for items in ar:
        for item in items:
            single_list.append(item)
    return single_list


print("task 7:", flatten(task_7))

# task 8, find median
print("_" * 100)
task_8 = []
for _ in range(10):
    task_8.append(random.randint(10, 20))

print(task_8)


def find_median(ar):
    ar.sort()
    half_size_len = len(ar) // 2
    elements = ar[half_size_len - 1: half_size_len + 1]
    return (elements[0] + elements[1]) / 2


print("task 8:", find_median(task_8))

# task 9, find mean
print("_" * 100)
task_9 = []
for _ in range(10):
    task_9.append(random.randint(10, 20))

print(task_9)


def find_mean(ar):
    sm = 0
    for i in ar:
        sm = sm + i
    return sm / len(ar)


print("task 9:", find_mean(task_9))

# task 10, lucky number test
print("_" * 100)


def is_my_ticket_lucky(ticket_number):
    result_first, result_second = int(), int()
    ticket_str = str(ticket_number)
    half_ticket_len = len(ticket_str) // 2
    res_first_set, res_second_set = ticket_str[:half_ticket_len], ticket_str[half_ticket_len:]

    for item_first in res_first_set:
        result_first += int(item_first)

    for item_second in res_second_set:
        result_second += int(item_second)

    return result_first == result_second


print(f'task 10: {is_my_ticket_lucky(123213)}')

# task 11, count qty of similar chars in string
print("_" * 100)
test_string = 'afdfghtttiioooayyyyyyyyyy'


def count_chars(str: str):
    for item in sorted(set(str)):
        qty_of_items_in_obj = str.count(item)
        print(f'qty of {item} in {str} is {qty_of_items_in_obj}')


print('task 11:')
count_chars(test_string)

# task 12, draw triangle
print("_" * 100)


#
###
#####
#######
#########
###########

def draw_triangle(r):
    for x in range(r):
        print(' ' * (r - x - 1) + '#' * (2 * x + 1))


draw_triangle(6)

# task 13, check int is prime number or not
print("_" * 100)


def is_prime(a: int):
    if a > 1:
        for x in range(2, a):
            if (a % x) == 0:
                print('not prime')
                break
        else:
            print('prime')
    else:
        print('not prime')


is_prime(33)

# task 14, given an array of ints, return true if the array contains either 3 even or 3 odd values all next to each other.
print("_" * 100)


def mod_three(nums: list) -> bool:
    even_count = int()
    odd_count = int()

    for n in nums:
        if n % 2 == 0:
            even_count += 1
            odd_count = 0
        else:
            odd_count += 1
            even_count = 0

        if even_count == 3 or odd_count == 3:
            return True
    return False


check_data = [
    ([2, 1, 3, 5], True),
    ([2, 1, 2, 5], False),
    ([2, 4, 2, 5], True)
]

for check, result in check_data:
    print(mod_three(check) == result)
