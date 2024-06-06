#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def verifChiffres(a,n):
    if n==0:
        v=True
    else:
        if 0<=a[n-1]<=9:
            v=verifChiffres(a,n-1)
        else:
            v=False

    return v

