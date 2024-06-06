#Commentaires
#Student number: 300262795 & 300090541
#Student name: Omar Benzekri & Jessica Longpré

def sequenceMax(l):
    count = 1
    maxCount = 1
    for i in range (len(l)-1):
        if l[i] == l[i+1]:
            count = count + 1
        else:
            maxCount = count if count > maxCount else maxCount            
            count = 1
    return max(maxCount, count)

l = list(eval(input(" Veuillez entrer une liste d'entiers séparées par des virgules: ")))
print(sequenceMax(l))
