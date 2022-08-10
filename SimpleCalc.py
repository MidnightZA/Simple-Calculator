# Messages to print
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

# Asks for an equation
while True:
    print(msg_0)
    calc = input()

    # Spilt into parts x, oper, y
    eq = calc.split()
    x = eq[0]
    oper = eq[1]
    y = eq[2]
    nums = [x, y]

# Check x or y NaN
    try:
        float(x)
    except ValueError:
        print(msg_1)
        continue
    else:
        x = float(x)
    try:
        float(y)
    except ValueError:
        print(msg_1)
        continue
    else:
        y = float(y)

#Check if oper is valid and perform calc.
    if oper not in ['+', '-', '*', '/']:
        print(msg_2)
        continue
    else:
        if oper == '+':
            print(x + y)
        elif oper == '-':
            print(x - y)
        elif oper == '*':
            print(x * y)
        elif oper == '/':
            try: x / y
            except ZeroDivisionError: print('y = 0, Try again')

    break
