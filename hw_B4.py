import random
a = random.randint(1, 100)
while 0!=1:
    b=input('������� ����� �� 1 �� 100: ')
    if not b.isdigit():
        print('������������ ����!')
    else:
        b=int(b)
        if b>100 or b<1:
            print('������������ ����!')
        else:
            if a > b:
                print('���������� ����� ������!')
            elif a < b:
                print('���������� ����� ������!')

            else:
                print('�������!�� �������!')
                quit()
