#Commentaires
#Student number: 300292795
#Student name: Omar Benzekri

import math
def fun(x):
    y = (math.log(x+3,10))/4
    return y
x = float(input("Entrez un nombre positif: "))
y = fun(x)
print("La solution y a votre equation est : ",y)
