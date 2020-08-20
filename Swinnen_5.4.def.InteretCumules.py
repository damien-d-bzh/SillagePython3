"""
Ce programme se propose de calculer la valeur finale d'une somme d'argent
epargnée à un taux indiqué par l'utilisateur après un nombre d'année, lui aissi
saisi par l'utilisateur
"""
def interetCumule(capital, taux, nombAnnee):
#capital=float(input("Entrée le montant du capital: "))
#nombAnnee=int(input("Entrée le nombre d'année :"))
#taux=float(input("Entrée le taux d'interet :"))
#print("Le valeur du compte d'epargne: "+str(capital*(1+(taux/100))**nombAnnee))
    return (capital*((1+(taux/100))**nombAnnee))

capital=float(input("Entrée le montant du capital: "))
nombAnnee=int(input("Entrée le nombre d'année :"))
taux=float(input("Entrée le taux d'interet :"))
print("La valeur de cet epargne est: ", str(interetCumule(capital, taux, nombAnnee)))
