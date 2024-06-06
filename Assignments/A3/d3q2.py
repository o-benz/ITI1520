#Commentaires
#Student number: 300262795 & 300090541
#Student name: Omar Benzekri & Jessica Longpré

import random

print("Ce logiciel va effectuez un test avec 10 questions")

ques=1
bonne_reponse = 0

def effectuezTest(op):
    a=0
    if(op==0):
        x=random.randint(0,9)
        y=random.randint(0,9)
        z=x+y
        question= str(x)+" + "+str(y)+" = "
        w= int(input(question))
        if w==z:
            a+=1
        elif w!=z:
            print("Incorrect - la reponse est",z)
    elif(op==1):
        x=random.randint(0,9)
        y=random.randint(0,9)
        z=x*y
        question= str(x)+" * "+str(y)+" = "
        w= int(input(question))
        if w==z:
            a+=1
        elif w!=z:
            print("Incorrect - la reponse est",z)
    return(a)
             

while ques <= 10:
    ques += 1
    op=random.randint(0,1)
    bonne_reponse += effectuezTest(op)


print(bonne_reponse," reponses correctes.")
if bonne_reponse<6:
    print("Demandez à votre enseignant(e) de vous aider.")
elif bonne_reponse>=6:
    print("Félicitations!")








