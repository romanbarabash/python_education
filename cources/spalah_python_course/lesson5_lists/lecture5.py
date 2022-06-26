"""
Slice any int from string
"""

a = "b098735bla bla"

b = 0
i = 0

while i < len(a):
    char = a[i]
    index = ord(char)
    num = index - ord('0')

    if num >= 0 and num <= 9:
        b = b * 10 + num

    i += 1

print(b)