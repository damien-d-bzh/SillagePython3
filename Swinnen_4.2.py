"""
Ce programme permet de converteir des Euros en Dollars après avoir
demandé à l'utilisateur de saisir le taux de change le plus récent
"""
import os
a=float(input("entrer la valeur du taux e change €/$: "))
i=1
while i<=16384:
    print(str(i)+" euro(s) = "+str(i*a)+" dollar(s)")
    i*=2 #multiplying i by 2
os.system("pause")
