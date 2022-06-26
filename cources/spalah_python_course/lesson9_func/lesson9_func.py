def sqrt(array):
    arr = []
    for item in array:
        arr.append(item * item)
    return arr


a = [2, 66]

print(sqrt(a))

to_format = "WE All aRE liVing In a dReam"


def title(str):
    is_first = True
    result = ' '
    for char in str:
        if char.isalpha():
            if not is_first:
                char = char.lower()
            else:
                char = char.upper()
                is_first = False
        else:
            is_first = True
        result += char
    return result


print(title(to_format))




