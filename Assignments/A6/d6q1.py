#Commentaires
#Student number: 300262795 & 300090541
#Student name: Omar Benzekri & Jessica Longpré

from random import shuffle
 
class Blackjack:
    valeurs={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}

    def joue(self):
        d = JeuDeCartes()
        d.battre()
        banque = Main('Banque')
        joueur = Main('Joueur')
        for i in range(2):
            joueur.ajouteCarte(d.tireCarte())
            banque.ajouteCarte(d.tireCarte())
        banque.montreMain()
        joueur.montreMain()
        reponse = input('Carte? Oui ou non? (Par défaut oui) ')
        while reponse in ['','o','O','oui','Oui']:
            c = d.tireCarte()
            print("Vous avez:")
            print(c)
            joueur.ajouteCarte(c)
            if self.total(joueur) > 21:
                print("Vous avez dépassé 21. Vous avez perdu.")
                return
            reponse = input('Carte? Oui ou non? (Par défaut oui) ')
        while self.total(banque) < 17:
            c = d.tireCarte()
            print("La banque a:")
            print(c)
            banque.ajouteCarte(c)
            if self.total(banque) > 21:
                print("La banque a dépassé 21. Vous avez gagné.")
                return
        self.compare(banque, joueur)
 
       
    def total(self, main):
        somme = 0
        somme_As = 0
        for carte in main.main:
            somme = somme + Blackjack.valeurs[carte.valeur]
            if Blackjack.valeurs[carte.valeur] == 'A':
                i += 1
        while somme > 21 and somme_As > 0:
            somme -= 10
            somme_As -=1
        return somme
 
    def compare(self, banque, joueur):
        banqueTotal = self.total(banque)
        joueurTotal = self.total(joueur)
        if banqueTotal > joueurTotal:
             print('Vous avez perdu.')
        elif banqueTotal < joueurTotal:
            print('Vous avez gagné.')
        if banqueTotal == 21 and 2 == len(banque.main) < len(joueur.main):
            print('Vous avez perdu.')
        elif (joueurTotal == 21) and 2 == len(banque.main) < len(joueur.main):
            print('Vous avez gagné.')
        else: print('Egalité.')
        
class Main(object):
 
    def __init__(self, joueur=str):
        self.joueur = joueur
        self.main = []
 
 
    def ajouteCarte(self, Carte):
        self.main.append(Carte)
 
    def montreMain(self):

        return print(self.joueur,':\n',self.main)
                 
    def __eq__(self, autre):
        return self.main == autre.main
 
    def __repr__(self):
        return 'Main('+str(self.main)+ ')'
    def GetVal(self):
        return self.valeur
    
class Carte:
 
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur 
    def __repr__(self):
        return 'Carte('+self.valeur+', '+self.couleur+')'
 
    def __eq__(self, autre):
        return self.valeur == autre.valeur and self.couleur == autre.couleur
 
 
class JeuDeCartes:
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
     
    def __init__(self):
        self.paquet = []          
        for couleur in JeuDeCartes.couleurs:
            for valeur in JeuDeCartes.valeurs:
                self.paquet.append(Carte(valeur,couleur))
 
    def tireCarte(self):
        return self.paquet.pop()
 
    def battre(self):
        shuffle(self.paquet)
 
    def __repr__(self):
        return 'Paquet('+str(self.paquet)+')'
 
    def __eq__(self, autre):
        return self.paquet == autre.paquet
     
     
b = Blackjack()
b.joue()
