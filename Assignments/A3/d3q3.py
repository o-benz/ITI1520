#Commentaires
#Student number: 300262795 & 300090541
#Student name: Omar Benzekri & Jessica Longpré

def compte_positifs(x):
    count = 0
    for i in x:
        if i > 0:
            count += 1
        else:
            count = count
    return(count)

x= input("Veuillez entrer une liste de valeurs séparées par des virgules: ")
x= list(eval(x))
print(compte_positifs(x))
