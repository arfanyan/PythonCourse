with open('rosalind_fib.txt') as file:
    s= file.readline().strip().split()
    k=int(s[0])
    n=int(s[1])
gen1=1
gen2=0
sum=0
a=0
while a<k:
    sum=gen1+gen2
    gen1=gen2*n
    gen2=sum
    a=a+1
print(sum)
