with open('file2.txt', 'w') as f:
    f.write('hello\n')
    f.write('world')

with open('file2.txt', 'r') as f:
    lines = list(f)
    print(lines)
