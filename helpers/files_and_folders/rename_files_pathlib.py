from pathlib import Path

p1 = Path('files/ghi.txt')
print(type(p1))

if not p1.exists():
    with open(p1, 'w') as file:
        file.write('Content 3')

print(p1.name)
print(p1.stem)
print(p1.suffix)

root_dir = Path('files')
file_paths = root_dir.iterdir()
for path in file_paths:
    new_filename = "demo-" + path.stem + path.suffix
    new_filepath = path.with_name(new_filename)
    print(new_filepath)
    path.rename(new_filepath)
