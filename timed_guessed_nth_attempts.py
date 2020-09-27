"""
ce script propose à l'utilisateur de deviner u  nombre entier relatif
en nth fois en un temps donné, le ninuteur n'est pas complétement
au point, mais la base est là
"""
import random
import os
import time
import datetime

#print(duree)
#duree+=time.localtime().tm_sec
#print(duree)
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
    duree=int(input("En combien de second le joueur doit-il deviner le bonne nombre: "))
    duree+=time.localtime().tm_sec
    #print(duree)
    print()
    n = int(input(f"Essayer de deviner le premier nombre entre 0 et {nombreMax} :"))
    i=1
    while (i<=tenttive):
        #print(i)
        if n<target and (duree>time.localtime().tm_sec):
            temp_restant=duree-time.localtime().tm_sec
            print(f"Il vous reste {temp_restant} seconces pour trouvé")
            n = int(input(f"Essayer de deviner le nombre plus grand entre 0 et {nombreMax} :"))
        elif n>target and (duree>time.localtime().tm_sec):
            temp_restant=duree-time.localtime().tm_sec
            print(f"Il vous reste {temp_restant} secondes pour trouvé")
            n = int(input(f"Essayer de deviner le nombre plus petit entre 0 et {nombreMax} :"))
        elif n==target and (duree>time.localtime().tm_sec):
            print("bravo")
            break
        elif n==target and (duree<time.localtime().tm_sec):
            print("Presque, mais trop tard")
            break
        elif duree<time.localtime().tm_sec:
            print("trop tard, perdu")
            break
        i+=1
Deviner()
os.system("pause")
