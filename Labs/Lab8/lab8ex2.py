#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def somme_matrices(a,b):
    i=0
    c=[]
    while i < len(a):
        j=0
        c.append([])
        while j < len(a[0]):
            c[i].append(a[i][j] + b[i][j])
            j+=1
        i+=1
    return c

a=[[0,1],[2,3]]
b=[[4,5],[6,7]]

print("c", somme_matrices(a,b))
