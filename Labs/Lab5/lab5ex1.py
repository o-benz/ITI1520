#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def moyenne(x):
    s=0
    for elem in x:
        s+=elem
    return s/len(x)

i=input("Veuillez entrer une liste de valeurs séparés par des virgule: ")
i=list(eval(i))
print(i)
print("La moyenne est:", moyenne(i))
