a=[int(i) for i in input('Введите числа через пробел: ').split()]
b=(a[0])
c=[]
for i in a:
    if i>b:
        c.append(i)
        b=i
    else:
        b=i
print('Числа, которые больше предыдущего: ', end='')
for i in c:
    print(i, end=' ')
