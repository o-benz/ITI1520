#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

class CompteBancaire:
    def __init__(self,nom='Dupont',solde=1000):
        self.nom, self.solide=nom,solde

    def depot(self,somme):
        self.solde+=somme

    def retrait(self,somme):
        self.solde-=somme
        
    def affiche(self):
        print(f"Le solde du compte bancaire de {self.nom} est de {self.solde} dollars.")

class CompteEpargne(CompteBancaire):
    def __init__ (self,nom='Dupont',solde=1000):
        CompteBancaire.__init__(self,nom,solde)
        self.taux=0.3
        
    def changeTaux(self,taux):
        self.taux=taux
        
    def capitalisation(self,nombreMois):
        print(f"Capitalisation sur {nombreMois} mois au taux mensuel de {self.taux} %.")
        for m in range(nombreMois):
            self.solde*=(100+self.taux)/100
        
