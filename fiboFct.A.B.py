"""
Part du principe de la suite de Fibonacce mais en laissant l'utilisateur
choisir les deux premiers termes et en imprimant à l'ecran l'ensemble des
valeures de la suite ainsi conçu sans dépasser la valeur max
"""
import os
def fibo(a, b, n):
    i=1
    while i<=n:
        t=a
        a=b
        b+=t
        i+=1
    return t

a=int(input("entrer le premier terme de la suite: "))
b=int(input("entrer le deuxième terme de la suite: "))
n=int(input("entrer le nombre max de calcul: "))
j=1
while j<=n:
    print(j,' ',fibo(a, b, j))
    j+=1
os.system("pause")
