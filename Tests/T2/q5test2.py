# Omar Benzekri, 300262795
#
# En mettant votre nom ici, vous signez la déclaration d'intégrité de q4test2 


#########################
# QUESTION 5
#########################            
    
def tanganyika(L):
    Q=[]
    for i in range(len(L)-1):
        if L[i]!=0:
            Q.append(L[i])
        if L[i]==0 and L[i+1]!=0:
            Q.append(L[i])
    if L[len(L)-1]==0 and Q[len(Q)-1]!=0:
        Q.append(L[len(L)-1])
    return Q


