#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def espaces(s):
    s2=""
    for c in s:
        s2+=c+" "
    s2=s2[:-1]
    return s2

s= input ("Entrez une chaine: ")
print("//"+espaces(s)+"//")
