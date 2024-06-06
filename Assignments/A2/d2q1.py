#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

w = float(input("SVP entre votre poids en kilogrammes: "))
h = float(input("SVP entre votre taille en metres: "))
def getBmi(w, h):
    imc = w / h ** 2
    return(imc)
imc=getBmi(w, h)
print("Votre IMC est",imc)
if imc < 18.5:
    print("Maigreur")
elif imc < 25:
    print("Poids ideal")
elif 25<= imc <30 :
    print("Surpoids")
else:
    print("Obésité")
    
