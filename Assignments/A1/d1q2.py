#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def convertEnKilos(lbs):
    "Transforme des livres en kilos"
    kg = lbs / 2.2046 + oz / 35.5274
    return kg
lbs = int (input("Entrez le nombre de livres: "))
oz = int (input("Entrez le nombre d’onces: "))
kg = convertEnKilos(lbs)
print(lbs,"livres et ",oz,"onces équivalent à ",kg,"kilogrammes")
