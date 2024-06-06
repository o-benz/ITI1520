#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

temp = float(input("Veuillez entrer la température: "))

if temp>=80:
    numAct=1

elif temp>=60 and temp<80:
    numAct=2

elif temp>=40 and temp<60:
    numAct=3

else:
    numAct=4

if numAct==1:
    print("L'activité recommandée est la natation")

elif numAct==2:
    print("L'activité recommandée est le soccer")

elif numAct==3:
    print("L'activité recommandée est le volleyball")

else:
    print("L'activité recommandée est le ski")


