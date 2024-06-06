
'''
Je comprends l'importance de l'intégrité professionnelle dans mes études et ma future carrière
en ingénierie ou en informatique. Je certifie par la présente que j'ai effectué et que je ferai tous les travaux
sur cet examen entièrement par moi-même, sans aide extérieure ou utilisation de matériel non autorisé
sources d'informations. De plus, je ne fournirai pas d'aide aux autres.
'''

# LIRE LA DÉCLARATION CI-DESSUS
#
# Omar Benzekri, 300262795
#
# En mettant votre nom ici, vous signez la déclaration ci-dessus et
# accepter le TEST 2 (règles d'intégrité)

#########################
# QUESTION 4
#########################

def nyasa(L):
    L2=[]
    c=0
    a=0
    for i in range(len(L)):
        L2.append(len(L[i]))

    for j in range(len(L2)):
        if L2.count(L2[j])!=1:
            c+=L2.count(L2[j])-1
    return c//2
