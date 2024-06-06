#Commentaires
#Student number: 300262795 & 300090541
#Student name: Omar Benzekri & Jessica Longpré

import random

print("Ce logiciel va effectuez un test avec 10 questions")
op=int(input("SVP choisissez l'operation 0) Addition 1) Multiplication (0 ou 1): "))
ques=1

def effectuezTest(ques, op):
    a=0
    if(op==0):
        while ques<=10:
            x=random.randint(0,9)
            y=random.randint(0,9)
            z=x+y
            question= str(x)+" + "+str(y)+" = "
            w= int(input(question))
            if w==z:
                a+=1
            elif w!=z:
                print("Incorrect - la reponse est",z)
            ques+=1
    elif(op==1):
        while ques<=10:
            x=random.randint(0,9)
            y=random.randint(0,9)
            z=x*y
            question= str(x)+" * "+str(y)+" = "
            w= int(input(question))
            if w==z:
                a+=1
            elif w!=z:
                print("Incorrect - la reponse est",z)
            ques+=1
    return(a)

a= effectuezTest(ques, op)
print(a," reponses correctes.")
if a<6:
    print("Demandez à votre enseignant(e) de vous aider.")
elif a>=6:
    print("Félicitations!")
                
            
            
    

