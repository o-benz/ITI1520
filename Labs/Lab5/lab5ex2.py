#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def statistiques(x):
    s=0
    minElem= x[0]
    maxElem= x[0]
    for elem in x:
        s+=elem
        if elem < minElem:
            minElem= elem
        if elem > maxElem:
            maxElem=elem
        
    m=s/len(x)
    return [m,maxElem,minElem]

i=input("Entrez les notes des etudiants: ")
i=list(eval(i))
s=statistiques(i)
print("Les notes des etudiants: ",i)
print("La moyenne est: ",s[0])
print("Le minimum est: ",s[2])
print("Le maximum est: ",s[1])
