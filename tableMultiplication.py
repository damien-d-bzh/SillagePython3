continuer="o"
while continuer=="o" or continuer=="O":
    a=int(input("entrer un nombre: "))
    while a<1 or a>9:
        print("préciser la table de multiplication")
        a = int(input("entrer un nombre: "))
    if a>=1 and a<=9:
        i=1
        while i<=10:
            print(a,'*', i,'=',a*i)
            i+=1
    continuer=input("Pour continuer 'o' ou 'O': ")
