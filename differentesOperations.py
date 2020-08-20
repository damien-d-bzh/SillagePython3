"""
un petit script sans autre intérêt que l'usage du module math
"""
import os
import math
a=int(input("Entrez un nombre 'a' pour la suite des operations: "))
b=int(input("Entrez un nombre 'b' pour la suite des operations: "))
c=float(input("Entrez un nombre 'c' pour la suite des operations: "))
# print("c: ", c, type(c))
# d=b/a
# print("d: ", d, type(d))
# e=b//a
# print("e: ", e, type(e))
f=b%a
print("b%a: ", f, type(f))
g=math.pow(a,2)
print("math.pow(): ", g, type(g))
h=math.sqrt(b)
print("math.sqrt(): ", h, type(h))
i=math.sin(c)
print("math.sin(c): ", i, type(i))
os.system("pause")
