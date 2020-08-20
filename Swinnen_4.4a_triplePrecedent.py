"""
Ce programme est une implémentation de la suite de Fibonacci
"""
import os
a,b,c=1,0,0
#print(str(c)+" "+str(b))
while c<=15:
    a,b,c=b,a+b,c+1
    print(str(c)+" "+str(b))
#os.system("pause")
