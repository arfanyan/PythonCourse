a=[str(i) for i in input('Введите строку: ').split()]
b=a[0]
for i in a:
    if len(i)<len(b):
        b=i
    else:
        continue
print('Длина самого короткого слова: ', len(b))
