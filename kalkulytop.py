a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = input('Выберите действие: *, %, /, **, -, +, //  ->  ')
if c == '*':
    print(a * b)
elif c == '%':
    print(a % b)
elif c == '/':
    print(a / b)
elif c == '**':
    print(a ** b)
elif c == '-':
    print(a - b)
elif c == '+':
    print(a + b)
elif c == '//':
    print(a // b)
else:
    print('Данной операции нет в системе!')














