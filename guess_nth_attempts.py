"""
ce script propose à l'utilisateur de deviner u  nombre entier relatif
en nth fois
"""
import random
import os
def nombreA_Deviner(max):
    return random.randint(0,max)
def nombreDeTentative():
    return int(input("Entre le nombre de tentative disponible au joueur :"))
def Deviner():
    nombreMax=int(input("Valeur max pour fonction random : "))
    target=nombreA_Deviner(nombreMax)
    tenttive=nombreDeTentative()
    #print(target)
    #print(tenttive)
    n=int(input("Essayer de deviner le nombre entre 0 et "+str(nombreMax)+" :"))
    i=1
    while i<tenttive:
        #print(i)
        if n<target:
            n=int(input("Essayer un nombre plus grand entre 0 et "+str(nombreMax)+" :"))
        elif n>target:
            n=int(input("Essayer un nombre plus petit entre 0 et "+str(nombreMax)+" :"))
        else: break
        i+=1
    if n!=target:
        return "loupé"
    else:
        return "bravo"
print(Deviner())
os.system("pause")
