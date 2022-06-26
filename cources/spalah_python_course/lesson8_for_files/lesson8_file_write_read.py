"""
w - writable mode which overwrites file
r - readable mode
r+ - readable + writable mode
w+ - writable + readable mode

 """

f = open('file1.txt', 'w')
f.seek(15)
print("Verify point to start write: ", f.seek(0))

f.write('allah akbar!!!\n')

print("Verify what position of cursor: ", f.tell())
print("Verify if file is writable: ", f.writable())
print("Verify if file is readable: ", f.readable())

f.close()

f = open('file1.txt', 'r')
print(f.read())
f.close()


