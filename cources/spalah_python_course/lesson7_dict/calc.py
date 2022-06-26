a = input('Input a: ')
b = input('Input b: ')
operator = input('Operator [*, /]: ')
result = None

if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    if operator == '*':
        result = a * b
    elif operator == '/':
        result = a / b

if result is None:
    result = 'Incorrect'
print(result)
