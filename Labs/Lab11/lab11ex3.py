#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def pgcd(x,y):
    if x%y==0:
        resultat=y
    else:
        resultat=pgcd(y,x%y)
    return resultat

