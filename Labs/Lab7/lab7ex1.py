#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def histo_n(x):
    d={}
    for c in x:
        d[c]=d.get(c,0)+1
    return d
t= tuple(eval(input("Elements: ")))
histo=histo_n(t)
print(histo)
l=list(histo.items())
l.sort()
print(l)
