with open('rosalind_revc.txt') as file:
    a=file.read()
b=''
for i in a:
    if i=='A':
        b='T'+b
    elif i=='T':
        b='A'+b
    elif i=='C':
        b='G'+b
    elif i=='G':
        b='C'+b
print(b)
    
