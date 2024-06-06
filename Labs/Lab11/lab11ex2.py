#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def initListe(l,n):
    if n != 0:
        l.insert(0,n-1)
        initListe(l,n-1)
l=[]
n=int(input('Entrez un n: '))
initListe(l,n)
print(l)
