#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def inputmatrice():
    m = int(input("Entrez le nombre de rangees: "))
    n = int(input("Entrez le nombre de colonnes: "))
    matrice = []
    i = 0
    while (i < m):
        j = 0
        matrice.append([])
        while j < n:
            v = int(input("matrice["+str(i)+","+str(j) +"]="))
            matrice[i].append(v)
            j = j + 1
        i = i + 1
    return matrice

def affichematrice(matrice):
    for i in matrice:
        for j in i: 
            print(j, end=" ")
        print()
   
def transpose(A):
    At=[]
    C=0
    while C < len(A[0]):
        L=0
        At.append([])
        while L < len(A):
            At[C].append(A[L][C])
            L+=1
        C+=1
    return At
        

A=inputmatrice()
At=transpose(A)
affichematrice(At)
