list=[int(i) for i in input('Введите значения параматров a,b и c через пробел: ').split()]
a,b,c=list[0],list[1],list[2]
d=b**2-4*a*c
import math
if d==0:
    print('Корень квадратного уравнения: ', -b/2*a)
elif d<0:
    print('Действительных корней нет')
else:
    print('Корни квадратного уравнения: ', (-b+math.sqrt(d))/2*a, (-b-math.sqrt(d))/2*a)
