#Commentaires
#Student number: 300292795
#Student name: Omar Benzekri

def numMonnaie(x):
    "Prend le montant en dollars et calcule le nombre de pièces"
    y = (x//.25)+((x%.25)//.10)+(((x%.25)%.10)//.05)+((((x%.25)%.10)%.05)//.01)
    return y
x = float (input("Entrez le montant en dollars: "))
y = numMonnaie(x)
print("Le nombre minimal de pièces que le caissier peut rendre est: ",y)
