#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

import math

def distance(v,teta):
    tetar=math.pi/180*teta
    g=9.8
    d=((2)*(v**(2))*(math.cos(tetar))*(math.sin(tetar)))/g
    return d

def calculdistances(v):
    distances=[]
    for teta in range(0, 100, 10):
        distances.append(distance(v,teta))
    return distances

v = float(input("Entrez la vitesse initiale (m/s): "))
ds = calculdistances(v)
for i in range(len(ds)):
    print("Pour angle", i*10,"degres, la balle parcourt ",ds[i]," metres.")
    teta=i*10
    ds[i]

