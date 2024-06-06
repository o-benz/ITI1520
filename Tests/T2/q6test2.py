# Omar Benzekri, 300262795
#
# En mettant votre nom ici, vous signez la déclaration d'intégrité de q4test2 

#########################
# QUESTION 6
#########################

def baikal(L):
    c=1
    for i in range(len(L)-1):
        if abs(L[i]-L[i+1])!=c:
            return False
        c+=1
    return True
