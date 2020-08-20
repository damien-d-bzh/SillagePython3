"""
affiche une la table de multiplication de chiffre saisie par l'utilisateur,
et imprime à l'écran un asterix jusye apres les nombres multiples de multiple_de
"""
nombre=int(input("Entrer le facteur de multiplication : "))
multiple_de=int(input("Entrer le facteur multiple de : "))
i=1
while i<=20:
    result=nombre*i
    print(result, end=' ')
    if result%multiple_de==0:
        print('*', end=' ')
    i+=1
