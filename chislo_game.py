import random 

flag = True
a = input('Желаете поиграть? (да/нет):   ')
if a.lower() == 'нет':
    print('Хорошего вам дня!')
else:
    i = 0
    a = input('Введите ваше имя: ')
    while flag:
        ran = random.randint(1, 6)
        b = int(input('Выберите число от 0 до 5: '))
        i+=1
        if b != ran:
            print('Попробуйте ещё раз!')
        else:
            print('Вы угодали число!!')
            print(f'Попыток  {i} раз')
            a = input('Желаете поиграть? (да/нет):   ')
            if a == 'нет':
                flag = False









