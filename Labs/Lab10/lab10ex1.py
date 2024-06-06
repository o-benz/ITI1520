#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

class Voiture:
    def __init__(self,marque='Ford',couleur='rouge'):
        self.marque=marque
        self.couleur=couleur
        self.pilote='personne'
        self.vitesse=0

    def choix_conducteur(self,nom):
        self.pilote=nom

    def accelerer(self,taux,duree):
        if self.pilote=='personne':
            print('Pas de conducteur')
        else:
            self.vitesse++taux*duree

    def affiche_tout(self):
        print(f"{self.marque} {self.couleur} pilotee par {self.pilote}, vitesse={self.vitesse} m/s")

    def __repr__(self):
        return f"{self.marque} {self.couleur} pilotee par {self.pilote}, vitesse={self.vitesse} m/s"

    def __eq__(self,autre):
        return self.marque == autre.marque and \
               self.couleur == autre.couleur and \
               self.pilote == autre.pilote and \
               self.vitesse == autre.vitesse
    
