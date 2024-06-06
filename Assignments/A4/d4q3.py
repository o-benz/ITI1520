#Commentaires
#Student number: 300262795 & 300090541
#Student name: Omar Benzekri & Jessica Longpré

print("Les nombres cubes sont :")
for i in range(100,499):
    if int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3==i:
        print(i," = ",int(str(i)[0])," **3 + ",int(str(i)[1])," **3 + ",int(str(i)[2])," **3 = ",int(str(i)[0])**3," + ",int(str(i)[1])**3," + ",int(str(i)[2])**3)
