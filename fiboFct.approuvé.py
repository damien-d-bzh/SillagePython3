import os
def fibo(c):
    a=0
    b=1
    i=1
    while i<=c :
        t=a
        a=b
        b=a+t
        i+=1
    return t

n=int(input("entrer un nombre: "))
j=1
while j<=n:
    if j<10:
        print(j,'   ',fibo(j))
    if j>=10:
        print(j,' ',fibo(j))
    j+=1
os.system("pause")
