#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

a=float(input("Veuillez entrer la valeur de a: "))
b=float(input("Veuillez entrer la valeur de b: "))
c=float(input("Veuillez entrer la valeur de c: "))

discriminant=b**2-4*a*c

if discriminant<0:
    nbR=0
elif discriminant==0:
    nbR=1
elif discriminant>0:
    nbR=2

print(" Le nombre de racine réelles est",nbR)
