#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

import math

def moyenne(x):
    s=0
    for elem in x:
        s+=elem
    return s/len(x)

def ecarttype(x):
    m=moyenne(x)
    s=0
    for elem in x:
        s+=(elem-m)**2
    v=s/(len(x)-1)
    return math.sqrt(v)

i= input("Entrez une liste de valeurs séparés par des virgules: ")
i= list(eval(i))
print(i)
print("L'écart-type est", ecarttype(i))
