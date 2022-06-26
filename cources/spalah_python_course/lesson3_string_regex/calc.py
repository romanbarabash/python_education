oneInt = int(input("oneInt: "))
twoInt = int(input("twoInt: "))
oper = input('operator: ')
otvet = int()

if oper == "+":
    oneInt = int(input("oneInt: "))
    twoInt = int(input("twoInt: "))
    otvet = oneInt + twoInt
elif oper == "-":
    otvet = oneInt - twoInt
elif oper == "/":
    otvet = oneInt / twoInt
elif oper == "*":
    otvet = oneInt * twoInt
elif oper != "*" or "/" or "+" or "-":
    otvet = "You input incorrect operator"
else:
    "You specified incorrect data"

print(otvet)

# add, *, /, **, %
