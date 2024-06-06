#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

import random

def devine(n):
    nombre=0
    tentative=0
    
    while nombre !=n:
        tentative+=1
        nombre=int(input("Devinez le numéro: "))
        
        if nombre>n:
            print("Trop haut!")
            
        if nombre<n:
            print("Trop bas!")
        
    return tentative

n= random.randint(1,10)
tentative=devine(n)

print("Bravo, vous avez trouvez le numéro en",tentative,"tentatives!")
