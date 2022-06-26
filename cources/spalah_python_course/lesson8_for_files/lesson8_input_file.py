with open('numbers.txt', 'w') as file:
    while True:
        n = input('Number: ')
        if n == 'q':
            break
        if not n.isdigit():
            print('Incorrect')
            break

        file.write(n + '\n')

with open('numbers.txt') as file:
    for (idx, line) in enumerate(sorted(file, key=int), 1):
        number = int(line)
        print(idx, ':', number)
