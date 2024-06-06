#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def compteV1(s,c):
    return s.count(c)

def compteV2 (s,c):
    count=0
    for x in s:
        if x==c:
            count+=1
    return count

s=input("Entrez une chaine: ")
print(compteV1 (s,'a'))
print(compteV2 (s,'a'))
