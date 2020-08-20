"""
Ceci est un 'programme' qui se propose de convertir un nombre de seconde
en minutes, heures, jours et semaines correspondentes.
"""
seconde=int(input("Entre le nombre de seconde à convertir : "))
secondesRestantes=seconde%60
minutes=seconde//60
print("secondes restantes : "+str(secondesRestantes)+" secondes à convtr "+str(seconde-secondesRestantes))
minutesRestantes= minutes%60
heures=minutes//60
print("minutes restantes : "+str(minutesRestantes))
heuresRestantes=heures%24
journee=heures//24
print("heures restantes : "+str(heuresRestantes))
journeeRestantes=journee%7
semaine=journee//7
print("nombres journee : "+str(journeeRestantes))
print("nombres semaine : "+str(semaine))
