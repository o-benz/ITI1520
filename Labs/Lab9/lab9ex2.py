#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def bubbleSort(l):
    echange=True
    NPas=0
    j=len(l)-1
    while echange:
        echange= False
        for i in range(j):
            NPas+=1
            if l[i]>l[i+1]:
                echange= True
                l[i],l[i+1]=l[i+1],l[i]
        j-=1
    print("Le nombre de pas est",NPas)
    return l
