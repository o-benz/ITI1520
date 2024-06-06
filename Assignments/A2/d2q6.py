#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

TOTAL = 20
MAX = 5
pile = TOTAL

print("Au tour du joueur 1. Il y a ",TOTAL,"pierres en tout.")

while pile>0:
    p1=int(input("Joueur 1: combien de pierres pouvez-vous déplacer? "))
    while not p1<=MAX and p1>=1:
        print("Nombre invalide, il doit être entre 1 et ",MAX,", et vous ne pouvez pas ramasser plus qu'il n'y en a dans la pile")
        p1= int(input("Joueur 1: combien de pierres pouvez-vous déplacer? "))
    pile=pile-p1
    if pile==0:
        win=str("Joueur 1")
        break
    elif pile<5:
        MAX=pile
    print("Au tour du joueur 2. Il y a ",pile," pierres en tout.")
    p2= int(input("Joueur 2: combien de pierres pouvez-vous déplacer? "))
    while not p2<=MAX and p2>=1:
        print("Nombre invalide, il doit être entre 1 et ",MAX,", et vous ne pouvez pas ramasser plus qu'il n'y en a dans la pile")
        p2= int(input("Joueur 2: combien de pierres pouvez-vous déplacer? "))
    pile=pile-p2
    if pile==0:
        win=str("Joueur 2")
        break
    elif pile<5:
        MAX=pile
    print("Au tour du joueur 1. Il y a ",pile," pierres en tout.")

print("Bravo,",win,"a gagné !")
print("Jeu terminé.")
