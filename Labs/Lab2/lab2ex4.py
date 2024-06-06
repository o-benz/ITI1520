#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

import math
def calcluleSurface(Côté1, Côté2, Côté3):
    "Calcule la surface d’un triangle."
    p = Côté1+Côté2+Côté3
    s = math.sqrt(p*(p-2*Côté1)*(p-2*Côté2)*(p-2*Côté3))/4
    return s

surface = calcluleSurface(20, 30, 40)

print("La surface du triangle est:",surface)
                          
