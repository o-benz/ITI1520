#Commentaires
#Student number: 300292795
#Student name: Omar Benzekri

def convertenSL(al):
    sl = al*31558464
    return sl
def convertenKM(sl):
    km = sl*300000
    return km

al =float (input("Entrez un nombre d’années-lumière: "))
sl =convertenSL(al)
km =convertenKM(sl)

print ("Le nombre de secondes-lumière est", sl)
print("La distance est",km,"km")

pe =float (input("Entrez la distance de la première étoile, en années-lumière: "))
de =float (input("Entrez la distance de la deuxième étoile, en années-lumière: "))

def distanceenKM(pe,de):
    dis=convertenKM(convertenSL(pe+de))
    return dis
dis =distanceenKM(pe,de)

print("La distance entre les deux étoiles est",dis,"km")
