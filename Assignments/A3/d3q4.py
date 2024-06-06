#Commentaires
#Student number: 300262795 & 300090541
#Student name: Omar Benzekri & Jessica Longpré

def sequenceDeDeux (x):
    l = len(x)
    for i in range(l-1):
            if x[i]==x[i+1]:
                return True
    return False

x= input("Veuillez entrer une liste de valeurs séparées par des virgules: ")
x= list(eval(x))

print(sequenceDeDeux(x))
