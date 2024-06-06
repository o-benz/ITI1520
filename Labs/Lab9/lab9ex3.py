#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def tri_par_insertion(l):
    NPas=0
    i=1
    while i<len(l):
        NPas+=1
        tmp=l[i]
        j=i-1
        while j>=0 and tmp<l[j]:
            NPas+=1
            l[j+1]=l[j]
            j-=1
        l[j+1]=tmp
        i+=1
    print('Le nombre de pas est',NPas)
    return l
