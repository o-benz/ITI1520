#Commentaires
#Student number: 300262795 & 300090541
#Student name: Omar Benzekri & Jessica Longpré

def inputmatrice():
    print("Entrez les nombres avec des espaces entre les colonnes.")
    print("Une rangee par ligne, et une ligne vide a la fin.")
    matrice = []
    while True:
        ligne = input()
        if not ligne: break
        valeurs = ligne.split()
        rangee = [int(val) for val in valeurs]
        matrice.append(rangee)
    return matrice

matrice=inputmatrice()
print("La matrice est:")
print(matrice)

def ajoute(matrice):
    m=[]
    for i in range(len(matrice)):
        r=[]
        for j in range(len(matrice[i])):
            r.append(matrice[i][j]+1)
        m.append(r)
    return m

matrice=ajoute(matrice)
print("Apres exécution de la fonction ajoute, la matrice est:")
print(matrice)

def ajoute_V2(matrice):
    m=[]
    for i in range(len(matrice)):
        r=[]
        for j in range(len(matrice[i])):
            r.append(matrice[i][j]+1)
        m.append(r)
    print(m)
            
print("Une nouvelle matrice crée avec ajoute_V2:")
ajoute_V2(matrice)
print("Apres exécution de la fonction ajoute_V2, la matrice initiale est:")
print(matrice)
    

            
    

