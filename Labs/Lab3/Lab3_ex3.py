#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

entier = int(input("Veuillez entrer un nombre entier: "))

if entier%2==0 and entier%3==0:
    divisible=1
elif entier%2==0 or entier%3==0:
    divisible=2
else:
    divisible=0

if divisible==1:
    print("L'entier",entier,"est divisible par 2 et 3")
elif divisible==2:
    print("L'entier",entier,"est divisible par 2 ou 3")
else:
    print("L'entier",entier,"n'est pas divisible ni par 2 ni par 3")
