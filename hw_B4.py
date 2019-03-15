import random
a = random.randint(1, 100)
while 0!=1:
    b=input('Введите число от 1 до 100: ')
    if not b.isdigit():
        print('Некорректный ввод!')
    else:
        b=int(b)
        if b>100 or b<1:
            print('Некорректный ввод!')
        else:
            if a > b:
                print('Загаданное число больше!')
            elif a < b:
                print('Загаданное число меньше!')

            else:
                print('Молодец!Вы угадали!')
                quit()
