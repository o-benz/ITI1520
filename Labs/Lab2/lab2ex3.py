#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def calcule(devoirsMoyenne, partiel, examen):
    "Calcule la note finale"
    note = devoirsMoyenne*25/100 + partiel*25/100 +examen*50/100
    return note

devoirsMoyenne = float (input("Entrez la moyenne des devoirs:"))
partiel = float (input("Entrez la note du partiel:"))
examen = float (input("Entrez la note de l'examen final:"))

note_final=calcule(devoirsMoyenne, partiel, examen)

print("La note finale est:",note)
