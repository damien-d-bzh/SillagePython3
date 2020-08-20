import os
height=int(input("Entrer la hauteur du sapin : "))
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

os.system("pause")
