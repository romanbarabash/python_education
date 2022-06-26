import random

numbers = []

for _ in range(10):
    numbers.append(random.randint(10, 20))

print(numbers)
numbers.sort()
print(numbers)

half_size = len(numbers) // 2
median = None

median = sum(numbers[half_size - 1: half_size + 1]) / 2

print(median)

# # find median with statistic module
# print(statistics.median(numbers))
