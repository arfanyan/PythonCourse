with open('rosalind_subs.txt') as file:
    string1 = file.readline().strip()
    string2 = file.readline().strip()
list1=[]
list2=[]
for i,j in enumerate(string1):
    if j==string2[0]:
        list1.append(i)
for i in list1:
    list2.append([i,string1[i:i+len(string2)]])
print('Позиции: ', end='')
for i in list2:
    if i[1]==string2:
        print(i[0]+1, end=' ')
    else:
        continue
