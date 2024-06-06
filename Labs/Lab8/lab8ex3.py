#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def produit_matrices(a,b):
    c=[]
    i=0
    while i<len(a):
        j=0
        c.append([])
        while j<len(b[0]):
            k=0
            c[i].append(0)
            while k<len(a[0]):
                c[i][j]+=a[i][k]*b[k][j]
                k+=1
            j+=1
        i+=1
    return c

a = [[1,2,3],[4,5,6]]
b = [[1,2],[3,4],[5,6]]
print(produit_matrices(a,b))
