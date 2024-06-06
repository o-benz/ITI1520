#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def coder(s):
    s2=""
    for i in range(0,len(s)-1,2):
        s2+= s[i+1]+s[i]
    return s2

s=input("Entrez une chaine: ")
print(coder(s))
