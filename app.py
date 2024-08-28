print('enter first number:')
s = input()
print('enter second number:')
s2 = input()
print('choose operation: +/-')
op = input()
match op:
    case "+":
        print(int(s)+ int(s2))

    case "-":
        print(int(s) - int(s2))

    case _:
        print("unknown operation")
