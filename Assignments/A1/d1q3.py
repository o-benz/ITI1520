#Commentaires
#Student number: 300292795
#Student name: Omar Benzekri

x = float (input("Entrez le montant en dollars: "))
y = x//.25
z = (x%.25)//.10
w = ((x%.25)%.10)//.05
v = (((x%.25)%.10)%.05)//.01
print("Le nombre minimal de pièces que le caissier peut rendre est: ",y+z+w+v)
