a=input('Введите положительное число: ')
b=0
c=1
for i in a:
    b+=int(i)
    c*=int(i)
print('Сумма цифр: ', b)
print('Произведение цифр: ', c)
