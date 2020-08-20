"""
Ce programme imprime à l'écran un arbre de la forme d'un sapin
dont la hauteur, ou plutôt nombre d'étage (pour ainsi dire) est
saisi par l'utilisateur et affiche un nombre paire d'étoile
"""
import os
def sapin(height):
#height=int(input("Entrer la hauteur du sapin : "))
#heightT=height
    i=1
    while i<=height:
        blank=height-i
        l=0
        while l<=blank:
            print(' ', end='')
            l+=1
        width=i+(i-1)
        j=1
        while j<=width:
            print('*', end='')
            j+=1
        print()
        i+=1

nmbre=int(input("Entrer la hauteur du sapin : "))
sapin(nmbre)
os.system("pause")
