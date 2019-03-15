
with open('rosalind_hamm.txt') as file:
    a=file.readline().strip()
    b=file.readline().strip()
c=0
d=0
for i in a:
    if i==b[c]:
        c+=1
    else:
        d+=1
        c+=1
print(d)
