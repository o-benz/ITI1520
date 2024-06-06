#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def recherche_binaire(l,v):
    NPas=1
    result=False
    i=0
    j=len(l)
    while i!=j+1:
        NPas+=1
        m=(i+j)//2
        if l[m]==v:
            result=True
            break
        elif l[m]<v:
            i=m+1
        else:
            j=m-1
    print('Le nombre de pas est', NPas)
    return result
