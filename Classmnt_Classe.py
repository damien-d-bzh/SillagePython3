"""
copyright Damien debroize
le 10/08/2020
un programe qui crée une liste d'élèves inscripts à une classe
enregistre leur notes et en calcule la moyenne
"""
import os
class UE_Eleves:
    def __init__(self, prenom, nom, moyene):
        self.prenom=prenom
        self.nom=nom
        self.moyene=moyene

    def moyenne(nots):
        somme=0
        notes=[]
        for i in range(nots):
            notes.append(int(input("Entre la note "+str(i+1)+" : ")))
            somme+=notes[i]
            print(somme)
        #
        print(notes)
        return somme/nots


nombsEleves=int(input("Entrer le nombre d'élève pour l'UE : "))
nts=int(input("Entrer le nombre de notes pour l'UE : "))
print("Il est proposé d'attribuer des notes à base de nombres entiers de 1 à 10")
print("commençons par rentrer le prénom et le nom de chaque élève puis leurs notes respectives: ")
eleves=[]
elevesNom=[]
elevesPrenom=[]
elevesMoyene=[]
for i in range(nombsEleves):
    #prenom=input("Entrer un prenom : ")
    #nom=input("Entrer un nom : ")
    #moyene=UE_Eleves.moyenne(nts)
    #print(type(moyene))
    eleves=UE_Eleves(input("Entrer un prenom : "), input("Entrer un nom : "), UE_Eleves.moyenne(nts))
    elevesNom.append(eleves.nom)
    elevesMoyene.append(eleves.moyene)
    elevesPrenom.append(eleves.prenom)
    #print(UE_Eleves.moyenne(nts))
    #print(eleves.prenom+" "+eleves.nom+" "+str(eleves.moyene))
#print(elevesNom,' ',elevesMoyene)
print()

for i in range(nombsEleves):
    print(elevesPrenom[i]+" "+elevesNom[i]+" "+str(elevesMoyene[i]))

Moyene=elevesMoyene.copy()
Moyene.sort()
print()
print()
print(elevesPrenom[nombsEleves-1]+" "+elevesNom[nombsEleves-1]+" "+str(elevesMoyene[nombsEleves-1]))
os.system("pause")
#UE_Eleves.Eleves(nombsEleves)ur l'UE : "))
#for i in range(nombsEleves):
#    print(taille_UE[i].prenom, taille_UE[i].nom, str(taille_UE[i].moyene))
