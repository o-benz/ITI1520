#Commentaires
#Student number: 300262795 & 300090541
#Student name: Omar Benzekri & Jessica Longpré

import random

def attend_le_joueur():
    try:
        input("Appuyez Enter pour continuer. ")
    except SyntaxError:
        pass
    
def prepare_paquet():
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663')
    return paquet

def donne_cartes(p):
    donneur=[]
    autre=[]

    paire = 0
    for loop in p:
        if paire%2 == 0:
            donneur.append(loop)
        else:
            autre.append(loop)
        paire = paire + 1
    return (donneur, autre)

def melange_paquet(p):
    random.shuffle(p)

def elimine_paires(l):
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    resultat=[]
    for carte in l:
        if carte[0]+carte[1] =='10':
            charactere = '10'
        else:
            charactere = carte[0]
        for couleur in couleurs:
            trouver = False
            if charactere + couleur in resultat:
                trouver = True
                resultat.remove(charactere + couleur)
        if trouver == False:
            resultat.append(carte)
    random.shuffle(resultat)
    return resultat

def affiche_cartes(p):
    for loop in p:
        print(loop, end="")
    print()

def entrez_position_valide(n):
    position = int(input("veuillez entrer un entier compris entre 1 et "+str(n)+": "))-1
    return position

def joue():
    p=prepare_paquet()
    melange_paquet(p)
    tmp=donne_cartes(p)
    donneur=tmp[0]
    humain=tmp[1]

    print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
    print("Votre main est:")
    affiche_cartes(humain)
    print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
    print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
    attend_le_joueur()

    donneur=elimine_paires(donneur)
    humain=elimine_paires(humain)
    tour = 1
    while len(humain)>=0 and len(donneur)>=0:
        print('***********************************************************')
        print('Votre tour.')
        print('Votre main est:')
        affiche_cartes(humain)
        print("J'ai ", len(donneur), "cartes. Si 1 est la position de ma première carte et ")
        print(len(donneur), "est la position de ma dernière carte, laquelle de mes cartes voulez-vous?")
        entree = entrez_position_valide(len(donneur))
        print("Vous avez demande ma ", entree+1,"eme carte.")
        print("La voilà. C'est un ", donneur[entree])
        print("Avec ", donneur[entree]," ajoute, votre main est:")
        humain.append(donneur[entree])
        donneur.remove(donneur[entree])
        affiche_cartes(humain)
        humain=elimine_paires(humain)
        if len(humain)==0:
            print("J'ai terminé toutes les cartes.")
            win = True
            break
        print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main est:")
        affiche_cartes(humain)
        attend_le_joueur()
        
        print('***********************************************************')
        print('Mon tour')
        prend_carte = random.randint(0,len(humain)-1)
        donneur.append(humain[prend_carte])
        humain.remove(humain[prend_carte])
        print("J'ai pris votre ", prend_carte+1,"eme carte")
        donneur=elimine_paires(donneur)
        if len(donneur)==0:
            print("J'ai terminé toutes les cartes.")
            win = False
            break
        attend_le_joueur()

    if win == True:
        print("Felicitations! Vous, Humain, vous avez gagne.")
    else:
        print("Vous avez perdu! Moi, Robot, j'ai gagne.")

joue()
