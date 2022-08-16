from pathlib import Path

p1 = Path('files/ghi.txt')
print(type(p1))

if not p1.exists():
    with open(p1, 'w') as file:
        file.write('Content 3')

print(p1.name)
print(p1.stem)
print(p1.suffix)

p2 = Path('files')
files_iterator = p2.iterdir()
file = next(files_iterator)  # abc.txt
