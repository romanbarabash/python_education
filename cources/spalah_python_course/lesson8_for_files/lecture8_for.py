a = [34, 67, 2, 56, 89, 100, 125]
a = 'hello'

print("show values with numbers")
for (idx, item) in enumerate(a, 1):
    print(idx, item)

print("show reversed list")
for item in reversed(a):
    print(item)

print("show sorted list")
for item in sorted(a):
    print(item)


