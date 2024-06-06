#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def calculeFact(n):
    res=1
    valeur=1
    while valeur<=n:
        res=res*valeur
        valeur =valeur+1
    return res
while True:
    n=int(input("Entrez un entier positif: "))
    if n>=0:
        break
    else:
        print("L'entier doit être supérieur ou égale à 0")
print("La factorielle de",n,"est",calculeFact(n))
