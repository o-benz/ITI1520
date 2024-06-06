#Commentaires
#Student number: 300262795 & 300090541
#Student name: Omar Benzekri & Jessica Longpré

# pas de boucles

# a)

def etoiles(n):
    if n == 0:
        return
    else:
        print(n * '*')
        etoiles(n-1)
        print(n * '*')

n = eval(input("SVP, Entrez un entier : "))
etoiles(n)

# b)

def sommeListePos_rec(l, n):
    n = len(l)
    if n >= 1:
        if l[0] > 0:
            return l[0] + sommeListePos_rec(l[1:], n-1)
        else:
            return sommeListePos_rec(l[1:], n-1)
    else:
        return 0

l = list(eval(input('Entrez une liste: ')))
print(sommeListePos_rec(l, len(l)))
