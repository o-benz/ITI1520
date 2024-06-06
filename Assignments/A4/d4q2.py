#Commentaires
#Student number: 300262795 & 300090541
#Student name: Omar Benzekri & Jessica Longpré

def nombre_divisible(l):
    count = 0
    for i in l:
        if i % n == 0:
            count += 1
        else:
            count = count
    return count

n = eval(input("SVP, Entrez un entier : "))
l = list(eval(input("Veuillez entrer une liste des valeurs séparées par des virgules: ")))

print(nombre_divisible(l))
         
